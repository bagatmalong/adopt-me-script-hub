"""Plugin registry — tracks slugs, versions, enable/disable state."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable


@dataclass
class PluginMeta:
    slug: str
    version: str
    path: str
    description: str = ""
    enabled: bool = True
    tags: list[str] = field(default_factory=list)


class PluginRegistry:
    def __init__(self) -> None:
        self._meta: dict[str, PluginMeta] = {}
        self._instances: dict[str, Any] = {}
        self.context: dict[str, Any] = {"registry": self}

    def register(self, meta: PluginMeta, instance: Any) -> None:
        if meta.slug in self._meta:
            raise ValueError(f"duplicate plugin slug: {meta.slug}")
        self._meta[meta.slug] = meta
        self._instances[meta.slug] = instance

    def instance(self, slug: str) -> Any | None:
        return self._instances.get(slug)

    def meta(self, slug: str) -> PluginMeta | None:
        return self._meta.get(slug)

    def all(self) -> Iterable[PluginMeta]:
        return list(self._meta.values())

    def enabled(self) -> Iterable[PluginMeta]:
        return [m for m in self._meta.values() if m.enabled]

    def set_enabled(self, slug: str, enabled: bool) -> None:
        if slug in self._meta:
            self._meta[slug].enabled = enabled

    def clear(self) -> None:
        self._meta.clear()
        self._instances.clear()