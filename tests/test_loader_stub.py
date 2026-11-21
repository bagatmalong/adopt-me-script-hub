from pathlib import Path

from adopt_me_hub.loader import ModuleLoader
from adopt_me_hub.registry import PluginRegistry


def test_loader_handles_missing_dir(tmp_path: Path):
    reg = PluginRegistry()
    loader = ModuleLoader(tmp_path / "does-not-exist", reg)
    assert loader.scan() == []
    assert loader.load_all() == 0


def test_loader_skips_private_files(tmp_path: Path):
    (tmp_path / "_helpers.py").write_text("x = 1\n")
    (tmp_path / "real.py").write_text(
        "PLUGIN_SLUG='real'\nPLUGIN_VERSION='1'\ndef setup(ctx):\n    return object()\n"
    )
    reg = PluginRegistry()
    loader = ModuleLoader(tmp_path, reg)
    loader.scan()
    assert loader.load_all() == 1
    assert reg.meta("real") is not None