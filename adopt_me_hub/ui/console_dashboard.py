"""Minimal console dashboard shown in the desktop shell."""
from __future__ import annotations

import sys


def render(registry) -> str:
    lines = ["adopt-me-script-hub  |  plugin host status", "-" * 44]
    for meta in registry.all():
        flag = "ON " if meta.enabled else "OFF"
        lines.append(f"[{flag}] {meta.slug:<16} v{meta.version:<10} {meta.description}")
    return "\n".join(lines)


def main(registry) -> int:
    sys.stdout.write(render(registry) + "\n")
    return 0