import pytest

from pytest_indigo import IndigoMock
from pytest_indigo.exceptions import ApiVersionException, NotImplementedException
from pytest_indigo.indigo.server import ServerInfo
from pytest_indigo.warnings import PartiallyImplementedWarning


# MARK: apiVersion
class TestApiVersion:
    def test_from_constructor(self):
        assert ServerInfo(api_version="3.4").apiVersion == "3.4"

    def test_mock_default(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "3"

    @pytest.mark.parametrize("indigo_api_version", ["2.4"])
    def test_from_fixture(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "2.4"

    def test_reset(self, indigo: IndigoMock):
        indigo.reset(api_version="1.8")

        assert indigo.server.apiVersion == "1.8"

    def test_reset_restores_default(self, indigo: IndigoMock):
        indigo.reset(api_version="1.8")
        indigo.reset()

        assert indigo.server.apiVersion == "3"


# MARK: getPluginList()
class TestGetPluginList:
    @pytest.mark.parametrize("indigo_api_version", ["1.8", "2.3"])
    def test_min_api(self, indigo: IndigoMock):
        with pytest.raises(ApiVersionException):
            indigo.server.getPluginList()

    @pytest.mark.parametrize("indigo_api_version", ["2.4", "2.5", "3"])
    def test_supported_api(self, indigo: IndigoMock):
        with pytest.warns(PartiallyImplementedWarning):
            assert indigo.server.getPluginList() == []

    def test_warns_partially_implemented(self, indigo: IndigoMock):
        with pytest.warns(PartiallyImplementedWarning):
            assert indigo.server.getPluginList() == []


# MARK: Not implemented
@pytest.mark.parametrize(
    "method",
    [
        "getDbName",
        "getDbFilePath",
        "getDeprecatedElems",
        "getInstallFolderPath",
        "getLogsFolderPath",
        "getLatitudeAndLongitude",
        "getReflectorURL",
        "getSerialPorts",
        "getWebServerURL",
        "removeAllDelayedActions",
        "savePluginPrefs",
        "sendEmailTo",
        "speak",
    ],
)
def test_not_implemented(indigo: IndigoMock, method):
    with pytest.raises(
        NotImplementedException,
        match=rf"^indigo\.server\.{method} has not been implemented by pytest-indigo!$",
    ):
        getattr(indigo.server, method)()
