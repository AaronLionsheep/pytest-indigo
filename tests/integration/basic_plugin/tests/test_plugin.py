import pytest

from ..plugin import Plugin


@pytest.mark.xfail(reason="Placeholder")
def test_can_create_plugin(indigo):
    plugin = Plugin()

    assert plugin.name == "plugin"


@pytest.mark.xfail(reason="Placeholder")
def test_can_start_plugin(indigo):
    plugin = Plugin()
    plugin.start()

    assert indigo.data.get("running")
