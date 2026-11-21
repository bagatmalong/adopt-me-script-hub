from __future__ import annotations

import argparse
from pathlib import Path

from adopt_me_hub.host import HostConfig, PluginHost
from adopt_me_hub.util import logger


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(prog="adopt-me-script-hub")
    ap.add_argument("--plugins", type=Path, default=Path("./plugins"))
    ap.add_argument("--list", action="store_true", help="list plugins and exit")
    return ap.parse_args()


def main() -> int:
    logger.configure()
    args = parse_args()
    host = PluginHost(HostConfig(plugins_dir=args.plugins))
    count = host.boot()
    if args.list:
        from adopt_me_hub.ui import console_dashboard
        return console_dashboard.main(host.registry)
    logger.configure().info("loaded %d plugin(s)", count)
    host.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())