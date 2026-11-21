"""Tracks the local player's pet inventory for quick plugin lookups."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PetEntry:
    name: str
    age: str = "Newborn"
    neon: bool = False
    mega: bool = False
    count: int = 1


@dataclass
class PetInventory:
    pets: dict[str, PetEntry] = field(default_factory=dict)

    def upsert(self, name: str, **kwargs) -> PetEntry:
        key = name.lower()
        entry = self.pets.get(key)
        if entry is None:
            entry = PetEntry(name=name, **kwargs)
            self.pets[key] = entry
        else:
            for k, v in kwargs.items():
                setattr(entry, k, v)
        return entry

    def remove(self, name: str) -> bool:
        return self.pets.pop(name.lower(), None) is not None

    def high_value(self, table: dict[str, int], threshold: int = 50) -> list[PetEntry]:
        return [p for p in self.pets.values() if table.get(p.name.lower(), 0) >= threshold]