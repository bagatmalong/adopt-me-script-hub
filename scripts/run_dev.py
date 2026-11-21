"""Convenience runner: boots the host with the bundled plugins folder."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from adopt_me_hub.host import HostConfig, PluginHost
from adopt_me_hub.util import logger


def main() -> int:
    logger.configure()
    host = PluginHost(HostConfig(plugins_dir=Path("adopt_me_hub/plugins")))
    loaded = host.boot()
    print(f"[dev] loaded {loaded} plugin(s)")
    for meta in host.registry.all():
        print(f"  - {meta.slug} v{meta.version}")
    host.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())