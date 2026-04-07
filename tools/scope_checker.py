"""Backward-compatible import — prefer roe_checker for new code."""

from roe_checker import ROEChecker as ScopeChecker

__all__ = ["ScopeChecker"]
