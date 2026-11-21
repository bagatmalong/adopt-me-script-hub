"""Egg sniper plugin — watches the nursery for rare egg drops."""
from __future__ import annotations

RARE_EGGS = {"safari", "jungle", "fossil", "royal", "danger"}

PLUGIN_SLUG = "egg-sniper"
PLUGIN_VERSION = "2026.0.7"
PLUGIN_DESCRIPTION = "Watches nursery UI for rare egg drops and auto-buys."


class EggSniper:
    def __init__(self, ctx):
        self.ctx = ctx
        self.seen: set[str] = set()

    def on_boot(self, ctx):
        pass

    def on_tick(self, payload):
        return None

    def on_trade_request(self, payload):
        return False

    def on_egg_hatch(self, payload):
        egg = (payload.get("egg") or "").lower()
        if egg in RARE_EGGS and egg not in self.seen:
            self.seen.add(egg)
            return {"buy": egg, "priority": "high"}
        return None

    def teardown(self):
        self.seen.clear()


def setup(ctx):
    return EggSniper(ctx)