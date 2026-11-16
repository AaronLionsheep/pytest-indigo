import pytest

from pytest_indigo import IndigoMock
from pytest_indigo.indigo import PluginBase


def test_fixture_returns_indigo_mock(indigo: IndigoMock):
    assert isinstance(indigo, IndigoMock)


def test_indigo_mock_type_parameter(indigo: IndigoMock[PluginBase]):
    """The plugin type parameter is only a type hint"""
    assert IndigoMock[PluginBase].__origin__ is IndigoMock  # type: ignore[attr-defined]
    assert isinstance(indigo.activePlugin, PluginBase)


@pytest.mark.xfail(reason="indigo.devices not implemented yet")
def test_fixture_returns_clean_indigo(indigo: IndigoMock):
    # ids should start at 1
    assert indigo.ids.peek() == 1

    assert len(indigo.devices) == 0


# MARK: indigo_api_version
class TestIndigoApiVersion:
    def test_default(self, indigo: IndigoMock, indigo_api_version):
        assert indigo_api_version == "3"
        assert indigo.server.apiVersion == "3"

    @pytest.mark.parametrize("indigo_api_version", ["2.4", "3.6"])
    def test_parametrize(self, indigo: IndigoMock, indigo_api_version):
        assert indigo.server.apiVersion == indigo_api_version

    def test_restored_after_parametrize(self, indigo: IndigoMock):
        """Runs after test_parametrize to check the version does not leak"""
        assert indigo.server.apiVersion == "3"

    def test_fixture_override(self, pytester: pytest.Pytester):
        pytester.makeconftest('pytest_plugins = ["pytest_indigo"]')
        pytester.makepyfile(
            """
            import pytest

            @pytest.fixture()
            def indigo_api_version():
                return "2.4"

            def test_api_version(indigo):
                assert indigo.server.apiVersion == "2.4"
            """
        )

        pytester.runpytest().assert_outcomes(passed=1)

    def test_ini_option(self, pytester: pytest.Pytester):
        pytester.makeconftest('pytest_plugins = ["pytest_indigo"]')
        pytester.makeini(
            """
            [pytest]
            indigo_api_version = 3.4
            """
        )
        pytester.makepyfile(
            """
            def test_api_version(indigo):
                assert indigo.server.apiVersion == "3.4"
            """
        )

        pytester.runpytest().assert_outcomes(passed=1)
