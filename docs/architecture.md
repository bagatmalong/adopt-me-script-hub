# Architecture

- `adopt_me_hub/host.py` — boots the loader, owns the registry, dispatches events
- `adopt_me_hub/loader.py` — scans the plugins directory and imports modules
- `adopt_me_hub/registry.py` — plugin metadata + instance map
- `adopt_me_hub/contracts/` — protocols plugins must satisfy
- `adopt_me_hub/bridge/` — IPC to a local executor, Roblox process discovery
- `adopt_me_hub/state/` — pet inventory + session persistence
- `adopt_me_hub/plugins/` — bundled reference plugins (pet-farmer, egg-sniper, trade-guard)
- `native/executor_bridge/` — C# helper for process discovery

The host is deliberately small: most behavior lives in plugins.