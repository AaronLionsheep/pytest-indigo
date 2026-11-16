import pytest
from plugin import Plugin

from pytest_indigo import IndigoMock


@pytest.mark.xfail(reason="Placeholder")
def test_can_create_plugin(indigo: IndigoMock):
    plugin = Plugin()

    assert plugin.name == "plugin"


@pytest.mark.xfail(reason="Placeholder")
def test_can_start_plugin(indigo: IndigoMock):
    plugin = Plugin()
    plugin.start()

    assert indigo.data.get("running")
