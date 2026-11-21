"""Event payload shapes emitted by the Adopt Me farming loop."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class FarmEvent:
    seq: int
    pet_name: str
    action: str  # "walk" | "sleep" | "eat" | "task"
    amount: int = 1
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class TradeEvent:
    seq: int
    partner: str
    offer_pets: list[str]
    request_pets: list[str]
    auto_accept: bool = False
    context: dict[str, Any] = field(default_factory=dict)