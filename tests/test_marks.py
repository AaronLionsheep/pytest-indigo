import pytest

from pytest_indigo import IndigoMock
from tests.test_plugin_fixture import make_plugin


@pytest.fixture()
def pytester(pytester: pytest.Pytester) -> pytest.Pytester:
    pytester.makeconftest('pytest_plugins = ["pytest_indigo"]')
    return pytester


def test_marks_registered(pytester: pytest.Pytester):
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.indigo_api_version("2.4")
        @pytest.mark.indigo_plugin_prefs({})
        def test_marks():
            pass
        """
    )

    pytester.runpytest("--strict-markers").assert_outcomes(passed=1)


# MARK: indigo_api_version
class TestIndigoApiVersion:
    @pytest.mark.indigo_api_version("2.4")
    def test_function_mark(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "2.4"

    @pytest.mark.indigo_api_version("2.4")
    @pytest.mark.parametrize("indigo_api_version", ["3.6"])
    def test_mark_overrides_parametrize(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "2.4"

    def test_without_mark(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "3"


@pytest.mark.indigo_api_version("2.4")
class TestIndigoApiVersionClassMark:
    def test_class_mark(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "2.4"

    @pytest.mark.indigo_api_version("3.6")
    def test_closest_mark(self, indigo: IndigoMock):
        assert indigo.server.apiVersion == "3.6"


def test_indigo_api_version_module_mark(pytester: pytest.Pytester):
    pytester.makepyfile(
        """
        import pytest

        pytestmark = pytest.mark.indigo_api_version("2.4")

        def test_module_mark(indigo):
            assert indigo.server.apiVersion == "2.4"

        @pytest.mark.indigo_api_version("3.6")
        def test_closest_mark(indigo):
            assert indigo.server.apiVersion == "3.6"
        """
    )

    pytester.runpytest().assert_outcomes(passed=2)


def test_indigo_api_version_mark_overrides_fixture(pytester: pytest.Pytester):
    pytester.makeconftest(
        """
        import pytest

        pytest_plugins = ["pytest_indigo"]

        @pytest.fixture()
        def indigo_api_version():
            return "3.6"
        """
    )
    pytester.makepyfile(
        """
        import pytest

        @pytest.mark.indigo_api_version("2.4")
        def test_mark(indigo):
            assert indigo.server.apiVersion == "2.4"

        def test_fixture(indigo):
            assert indigo.server.apiVersion == "3.6"
        """
    )

    pytester.runpytest().assert_outcomes(passed=2)


# MARK: indigo_plugin_prefs
def test_indigo_plugin_prefs_mark(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        import pytest

        @pytest.fixture()
        def plugin_prefs():
            return {"source": "fixture"}

        @pytest.mark.indigo_plugin_prefs({"source": "mark"})
        def test_mark_overrides_fixture(indigo, plugin):
            assert isinstance(plugin.plugin_prefs, indigo.Dict)
            assert plugin.plugin_prefs == {"source": "mark"}

        def test_without_mark(plugin):
            assert plugin.plugin_prefs == {"source": "fixture"}
        """
    )

    pytester.runpytest().assert_outcomes(passed=2)


def test_indigo_plugin_prefs_closest_mark(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        import pytest

        pytestmark = pytest.mark.indigo_plugin_prefs({"source": "module"})

        def test_module_mark(plugin):
            assert plugin.plugin_prefs == {"source": "module"}

        @pytest.mark.indigo_plugin_prefs({"source": "class"})
        class TestClassMark:
            def test_class_mark(self, plugin):
                assert plugin.plugin_prefs == {"source": "class"}

            @pytest.mark.indigo_plugin_prefs({"source": "function"})
            def test_function_mark(self, plugin):
                assert plugin.plugin_prefs == {"source": "function"}
        """
    )

    pytester.runpytest().assert_outcomes(passed=3)


def test_indigo_plugin_prefs_mark_copied_per_test(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        import indigo
        import pytest

        pytestmark = pytest.mark.indigo_plugin_prefs(indigo.Dict({"count": 0}))

        def test_first(plugin):
            plugin.plugin_prefs["count"] = 1

        def test_second(plugin):
            assert plugin.plugin_prefs == {"count": 0}
        """
    )

    pytester.runpytest().assert_outcomes(passed=2)


# MARK: Invalid marks
@pytest.mark.parametrize(
    ("mark", "error"),
    [
        pytest.param(
            "indigo_api_version()",
            r"The indigo_api_version mark takes a single str argument, but got args=() kwargs={}",
            id="api-version-missing",
        ),
        pytest.param(
            'indigo_api_version("2.4", "3.6")',
            r"The indigo_api_version mark takes a single str argument, but got args=('2.4', '3.6') kwargs={}",
            id="api-version-extra",
        ),
        pytest.param(
            "indigo_api_version(2.4)",
            r"The indigo_api_version mark takes a single str argument, but got args=(2.4,) kwargs={}",
            id="api-version-type",
        ),
        pytest.param(
            'indigo_api_version(version="2.4")',
            r"The indigo_api_version mark takes a single str argument, but got args=() kwargs={'version': '2.4'}",
            id="api-version-kwarg",
        ),
        pytest.param(
            "indigo_plugin_prefs()",
            r"The indigo_plugin_prefs mark takes a single dict argument, but got args=() kwargs={}",
            id="plugin-prefs-missing",
        ),
        pytest.param(
            'indigo_plugin_prefs([("key", "value")])',
            r"The indigo_plugin_prefs mark takes a single dict argument, but got args=([('key', 'value')],) kwargs={}",
            id="plugin-prefs-type",
        ),
    ],
)
def test_invalid_mark(pytester: pytest.Pytester, mark, error):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        f"""
        import pytest

        @pytest.mark.{mark}
        def test_invalid_mark(plugin):
            pass
        """
    )

    result = pytester.runpytest()

    result.assert_outcomes(errors=1)
    assert f"PytestIndigoException: {error}" in result.stdout.str()
