"""Discovers and imports plugin modules from the plugins directory."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from adopt_me_hub.registry import PluginMeta, PluginRegistry

REQUIRED_ATTRS = ("PLUGIN_SLUG", "PLUGIN_VERSION", "setup")


class ModuleLoader:
    def __init__(self, plugins_dir: Path, registry: PluginRegistry) -> None:
        self.plugins_dir = plugins_dir
        self.registry = registry
        self._paths: dict[str, Path] = {}

    def scan(self) -> list[Path]:
        if not self.plugins_dir.exists():
            return []
        found = []
        for path in sorted(self.plugins_dir.glob("*.py")):
            if path.name.startswith("_"):
                continue
            self._paths[path.stem] = path
            found.append(path)
        return found

    def load_all(self) -> int:
        count = 0
        for stem, path in self._paths.items():
            if self.load_one(stem, path):
                count += 1
        return count

    def load_one(self, stem: str, path: Path) -> bool:
        spec = importlib.util.spec_from_file_location(f"adopt_me_plugin_{stem}", path)
        if spec is None or spec.loader is None:
            return False
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        try:
            spec.loader.exec_module(module)
        except Exception:  # noqa: BLE001
            return False
        if not all(hasattr(module, attr) for attr in REQUIRED_ATTRS):
            return False
        meta = PluginMeta(
            slug=module.PLUGIN_SLUG,
            version=module.PLUGIN_VERSION,
            path=str(path),
            description=getattr(module, "PLUGIN_DESCRIPTION", ""),
        )
        try:
            instance = module.setup(self.registry.context)
        except Exception:  # noqa: BLE001
            return False
        self.registry.register(meta, instance)
        return True