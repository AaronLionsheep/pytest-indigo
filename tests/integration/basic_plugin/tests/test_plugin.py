from ..plugin import Plugin

def test_can_create_plugin(indigo):
    plugin = Plugin()

    assert plugin.name == "plugin"

def test_can_start_plugin(indigo):
    plugin = Plugin()
    plugin.start()

    assert indigo.data.get("running")