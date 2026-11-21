"""Trade-guard plugin — declines scam offers using a pet-value heuristic."""
from __future__ import annotations

PLUGIN_SLUG = "trade-guard"
PLUGIN_VERSION = "2026.2.0"
PLUGIN_DESCRIPTION = "Rejects lowball trades using a rough pet-value table."

VALUE_TABLE = {
    "shadow dragon": 100,
    "frost dragon": 80,
    "giraffe": 70,
    "bat dragon": 60,
    "neon dragon": 40,
    "turtle": 15,
    "unicorn": 8,
}


class TradeGuard:
    def __init__(self, ctx):
        self.ctx = ctx
        self.log: list[dict] = []

    def _value(self, pet: str) -> int:
        return VALUE_TABLE.get(pet.strip().lower(), 1)

    def on_boot(self, ctx):
        pass

    def on_tick(self, payload):
        return None

    def on_trade_request(self, payload):
        offered = sum(self._value(p) for p in payload.get("offer_pets", []))
        requested = sum(self._value(p) for p in payload.get("request_pets", []))
        decision = offered >= requested
        self.log.append({"offered": offered, "requested": requested, "ok": decision})
        return decision

    def on_egg_hatch(self, payload):
        return None

    def teardown(self):
        self.log.clear()


def setup(ctx):
    return TradeGuard(ctx)