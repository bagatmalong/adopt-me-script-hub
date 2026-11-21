"""Watches for a Roblox process and exposes the executor attach stub."""
from __future__ import annotations

import subprocess
from dataclasses import dataclass


@dataclass
class RobloxProcess:
    pid: int
    path: str


def find_roblox() -> RobloxProcess | None:
    try:
        out = subprocess.check_output(
            ["tasklist", "/FI", "IMAGENAME eq RobloxPlayerBeta.exe", "/FO", "CSV", "/NH"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    for line in out.splitlines():
        parts = [p.strip('"') for p in line.split(",")]
        if len(parts) >= 2 and parts[0].lower().startswith("robloxplayerbeta"):
            try:
                return RobloxProcess(pid=int(parts[1]), path="RobloxPlayerBeta.exe")
            except ValueError:
                continue
    return None


def attach_stub(pid: int) -> bool:
    """Placeholder for executor attach — real builds swap in the Lua injector."""
    return pid > 0