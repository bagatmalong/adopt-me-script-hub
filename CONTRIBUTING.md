# Contributing to adopt-me-script-hub

Thanks for wanting to help! This is a hobbyist plugin host for Roblox Adopt Me
script modules. Keep contributions focused and small.

## Adding a plugin

1. Drop a `.py` file in `adopt_me_hub/plugins/` (or your own `plugins/` dir).
2. Export `PLUGIN_SLUG`, `PLUGIN_VERSION`, `PLUGIN_DESCRIPTION`, and `setup(ctx)`.
3. The object returned by `setup` should implement the `AdoptMePlugin` protocol
   from `adopt_me_hub/contracts/plugin_base.py`.

## Style

- Python 3.11+, `from __future__ import annotations` in every module.
- Keep plugin modules under ~200 lines.
- No new dependencies without discussion in an issue.

## Testing

```bash
pip install -r requirements.txt
pytest -q
```

## Scope

This project is for educational / research use against your own Roblox
sessions. Do not submit plugins that target other players, scrape Roblox
account credentials, or automate trades without user confirmation.