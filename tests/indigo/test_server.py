import pytest

from pytest_indigo import IndigoMock
from pytest_indigo.exceptions import ApiVersionException, NotImplementedException
from pytest_indigo.warnings import PartiallyImplementedWarning


class TestGetPluginList:
    def test_min_api(self, indigo: IndigoMock):
        indigo.server._api_version = "1.8"

        with pytest.raises(ApiVersionException):
            indigo.server.getPluginList()

    def test_warns_partially_implemented(self, indigo: IndigoMock):
        with pytest.warns(PartiallyImplementedWarning):
            assert indigo.server.getPluginList() == []


def test_get_db_name(indigo: IndigoMock):
    with pytest.raises(NotImplementedException):
        indigo.server.getDbName()
