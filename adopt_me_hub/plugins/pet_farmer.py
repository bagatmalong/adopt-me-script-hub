"""Auto-farm plugin — walks pets, feeds them, and claims tasks."""
from __future__ import annotations

PLUGIN_SLUG = "pet-farmer"
PLUGIN_VERSION = "2026.1.4"
PLUGIN_DESCRIPTION = "Auto-farm Adopt Me pets: walk, sleep, eat, task claim."


class PetFarmer:
    def __init__(self, ctx):
        self.ctx = ctx
        self._claim_queue: list[str] = []
        self._task_ticks = 0

    def on_boot(self, ctx):
        self._claim_queue.extend(["sleep", "eat", "walk"])

    def on_tick(self, payload):
        self._task_ticks += 1
        if self._task_ticks % 30 != 0 or not self._claim_queue:
            return None
        action = self._claim_queue.pop(0)
        return {"action": action, "target": payload.get("pet", "default")}

    def on_trade_request(self, payload):
        return False

    def on_egg_hatch(self, payload):
        return None

    def teardown(self):
        self._claim_queue.clear()


def setup(ctx):
    return PetFarmer(ctx)