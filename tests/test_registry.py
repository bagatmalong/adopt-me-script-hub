from adopt_me_hub.registry import PluginMeta, PluginRegistry


class Dummy:
    def on_tick(self, payload):
        return {"ok": True}


def test_register_and_lookup():
    reg = PluginRegistry()
    meta = PluginMeta(slug="dummy", version="0.0.1", path="dummy.py")
    reg.register(meta, Dummy())
    assert reg.instance("dummy") is not None
    assert reg.meta("dummy").version == "0.0.1"
    assert [m.slug for m in reg.enabled()] == ["dummy"]


def test_disable_hides_from_enabled():
    reg = PluginRegistry()
    reg.register(PluginMeta(slug="x", version="1", path="x.py"), Dummy())
    reg.set_enabled("x", False)
    assert list(reg.enabled()) == []