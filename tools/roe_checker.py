"""
Rules of engagement (ROE) — deterministic hostname allowlist.

Same anchored suffix matching as legacy scope checks: code-based, not LLM judgment.
Use for any HTTP(S) surface (OWA, AD FS, certificate enrollment web) during AD engagements.

  - "*.corp.local" matches "dc01.corp.local" but NOT "evil-corp.local"
  - "corp.local" matches exactly "corp.local"
"""

import sys
from urllib.parse import urlparse


class ROEChecker:
    """Validate targets against ROE allow/deny lists before outbound connections."""

    def __init__(
        self,
        domains: list[str],
        excluded_domains: list[str] | None = None,
        excluded_classes: list[str] | None = None,
    ):
        self.domains = [d.lower() for d in domains]
        self.excluded_domains = [d.lower() for d in (excluded_domains or [])]
        self.excluded_classes = [c.lower() for c in (excluded_classes or [])]

    def is_in_scope(self, url: str) -> bool:
        if not url or not isinstance(url, str):
            return False
        normalized = url if "://" in url else f"https://{url}"
        try:
            parsed = urlparse(normalized)
        except Exception:
            return False
        hostname = parsed.hostname
        if not hostname:
            return False
        hostname = hostname.lower()
        if _is_ip(hostname):
            print(
                f"WARNING: ROE checker does not support bare IP hostnames: {hostname}",
                file=sys.stderr,
            )
            return False
        for excluded in self.excluded_domains:
            if _domain_matches(hostname, excluded):
                return False
        for pattern in self.domains:
            if _domain_matches(hostname, pattern):
                return True
        return False

    def is_vuln_class_allowed(self, vuln_class: str) -> bool:
        return vuln_class.lower() not in self.excluded_classes

    def filter_urls(self, urls: list[str]) -> tuple[list[str], list[str]]:
        in_scope = []
        out_of_scope = []
        for url in urls:
            if self.is_in_scope(url):
                in_scope.append(url)
            else:
                out_of_scope.append(url)
        return in_scope, out_of_scope

    def filter_file(self, input_path: str, output_path: str | None = None) -> tuple[int, int]:
        with open(input_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        in_scope, out_of_scope = self.filter_urls(lines)
        dest = output_path or input_path
        with open(dest, "w") as f:
            for url in in_scope:
                f.write(url + "\n")
        if out_of_scope:
            print(
                f"WARNING: filtered {len(out_of_scope)} out-of-ROE URLs from {input_path}",
                file=sys.stderr,
            )
        return len(in_scope), len(out_of_scope)


def _domain_matches(hostname: str, pattern: str) -> bool:
    if pattern.startswith("*."):
        suffix = pattern[1:]
        return hostname.endswith(suffix) and hostname != suffix[1:]
    return hostname == pattern


def _is_ip(hostname: str) -> bool:
    if hostname.startswith("[") or ":" in hostname:
        return True
    parts = hostname.split(".")
    if len(parts) == 4:
        try:
            return all(0 <= int(p) <= 255 for p in parts)
        except ValueError:
            return False
    return False


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(description="ROE / hostname allowlist check")
    p.add_argument("--target", required=True, help="URL or hostname to test")
    p.add_argument(
        "--config",
        default="",
        help="JSON config with roe_allowed_domains / roe_excluded_domains",
    )
    args = p.parse_args()
    domains = ["*.local"]
    excluded = []
    if args.config:
        import json
        with open(args.config) as f:
            cfg = json.load(f)
        domains = cfg.get("roe_allowed_domains") or cfg.get("domains") or domains
        excluded = cfg.get("roe_excluded_domains") or cfg.get("excluded_domains") or []
    chk = ROEChecker(domains, excluded)
    ok = chk.is_in_scope(args.target)
    print("ALLOW" if ok else "DENY", args.target)
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
