# Security Policy

## Reporting a vulnerability

Open a private security advisory on GitHub, or email the maintainers listed in
`pyproject` metadata. Please do not file public issues for anything that could
be used to attack other players.

## Scope

In scope:
- Crashes in the plugin host or the loader
- Bugs that cause plugin code to execute outside its sandbox expectations
- IPC bridge flaws in `adopt_me_hub/bridge/`

Out of scope:
- Bans applied by Roblox for using this tool (use at your own risk)
- The quality of any third-party plugin dropped into `plugins/`
- Issues in the native `executor_bridge` that only affect unsupported .NET
  versions

## Hardening notes

- Plugins run in-process. Treat anything in `plugins/` as trusted code.
- The IPC bridge binds to `127.0.0.1` only. Do not change this without a
  strong reason.