"""Persists lightweight session state between hub runs."""
from __future__ import annotations

import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".adopt-me-script-hub" / "session.json"


class SessionStore:
    def __init__(self, path: Path = DEFAULT_PATH) -> None:
        self.path = path
        self._data: dict = {}

    def load(self) -> dict:
        if not self.path.exists():
            return {}
        try:
            self._data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            self._data = {}
        return self._data

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self._data, indent=2), encoding="utf-8")

    def get(self, key: str, default=None):
        return self._data.get(key, default)

    def set(self, key: str, value) -> None:
        self._data[key] = value