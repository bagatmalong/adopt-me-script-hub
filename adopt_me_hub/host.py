"""Core plugin host. Boots the loader, wires the registry, dispatches events."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from adopt_me_hub.loader import ModuleLoader
from adopt_me_hub.registry import PluginRegistry, PluginMeta

log = logging.getLogger("adopt_me.host")


@dataclass
class HostConfig:
    plugins_dir: Path = Path("./plugins")
    auto_reload: bool = True
    roblox_pid_hint: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)


class PluginHost:
    def __init__(self, config: HostConfig) -> None:
        self.config = config
        self.registry = PluginRegistry()
        self.loader = ModuleLoader(config.plugins_dir, self.registry)

    def boot(self) -> int:
        self.loader.scan()
        loaded = self.loader.load_all()
        log.info("host booted with %d plugin(s)", loaded)
        return loaded

    def dispatch(self, event: str, payload: dict[str, Any]) -> list[Any]:
        results = []
        for meta in self.registry.enabled():
            plugin = self.registry.instance(meta.slug)
            if plugin is None:
                continue
            handler = getattr(plugin, f"on_{event}", None)
            if handler is None:
                continue
            try:
                results.append(handler(payload))
            except Exception as exc:  # noqa: BLE001
                log.exception("plugin %s failed on %s: %s", meta.slug, event, exc)
        return results

    def shutdown(self) -> None:
        for meta in self.registry.all():
            inst = self.registry.instance(meta.slug)
            if inst is not None and hasattr(inst, "teardown"):
                try:
                    inst.teardown()
                except Exception:  # noqa: BLE001
                    log.exception("teardown failed for %s", meta.slug)
        self.registry.clear()