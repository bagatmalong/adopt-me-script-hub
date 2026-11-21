# Plugin authoring guide

Every plugin is a plain Python module exposing a small, stable contract.

```python
PLUGIN_SLUG = "my-plugin"
PLUGIN_VERSION = "2026.1.0"
PLUGIN_DESCRIPTION = "Does the thing."

class MyPlugin:
    def on_boot(self, ctx): ...
    def on_tick(self, payload): ...
    def on_trade_request(self, payload): ...
    def on_egg_hatch(self, payload): ...
    def teardown(self): ...

def setup(ctx):
    return MyPlugin()
```

The host calls `on_tick` on every farm loop iteration, `on_trade_request`
when a trade window opens, and `on_egg_hatch` whenever the nursery detects an
egg. Return `False` from `on_trade_request` to auto-decline.