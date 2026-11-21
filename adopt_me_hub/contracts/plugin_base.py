"""Shared contract every Adopt Me script plugin must implement."""
from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class AdoptMePlugin(Protocol):
    """A plugin that hooks into the Roblox Adopt Me script hub pipeline."""

    def on_boot(self, ctx: dict[str, Any]) -> None: ...

    def on_tick(self, payload: dict[str, Any]) -> dict[str, Any] | None: ...

    def on_trade_request(self, payload: dict[str, Any]) -> bool: ...

    def on_egg_hatch(self, payload: dict[str, Any]) -> dict[str, Any] | None: ...

    def teardown(self) -> None: ...