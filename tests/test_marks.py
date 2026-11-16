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


@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        pytest.param(
            ['indigo_plugin_prefs({"key": "mark"}, merge=True)'],
            {"key": "mark", "other": "fixture"},
            id="merge",
        ),
        pytest.param(
            ['indigo_plugin_prefs(prefs={"key": "mark"}, merge=True)'],
            {"key": "mark", "other": "fixture"},
            id="merge-prefs-keyword",
        ),
        pytest.param(
            ['indigo_plugin_prefs({"key": None}, merge=True)'],
            {"key": None, "other": "fixture"},
            id="merge-none-value",
        ),
        pytest.param(
            ['indigo_plugin_prefs(unset=["key"])'],
            {"other": "fixture"},
            id="unset-merges-without-prefs",
        ),
        pytest.param(
            ['indigo_plugin_prefs(unset=("key", "missing"))'],
            {"other": "fixture"},
            id="unset-missing-key",
        ),
        pytest.param(
            ['indigo_plugin_prefs({"key": "mark"}, merge=True, unset=["key"])'],
            {"other": "fixture"},
            id="unset-after-merge",
        ),
        pytest.param(
            ['indigo_plugin_prefs({"key": "mark", "new": "mark"}, unset=["new"])'],
            {"key": "mark"},
            id="unset-after-replace",
        ),
        pytest.param(
            ["indigo_plugin_prefs()"],
            {"key": "fixture", "other": "fixture"},
            id="empty-merges",
        ),
        pytest.param(
            ["indigo_plugin_prefs(merge=False)"],
            {},
            id="empty-replace",
        ),
    ],
)
def test_indigo_plugin_prefs_modes(pytester: pytest.Pytester, marks, expected):
    make_plugin(pytester, "First")
    decorators = "\n".join(f"@pytest.mark.{mark}" for mark in marks)
    pytester.makepyfile(
        f"""
        import pytest

        @pytest.fixture()
        def plugin_prefs():
            return {{"key": "fixture", "other": "fixture"}}

        {decorators}
        def test_prefs(indigo, plugin):
            assert isinstance(plugin.plugin_prefs, indigo.Dict)
            assert plugin.plugin_prefs == {expected!r}
        """
    )

    pytester.runpytest().assert_outcomes(passed=1)


def test_indigo_plugin_prefs_layered_marks(pytester: pytest.Pytester):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        import pytest

        pytestmark = pytest.mark.indigo_plugin_prefs({"level": "module", "a": "module"})

        def test_module(plugin):
            assert plugin.plugin_prefs == {"level": "module", "a": "module"}

        @pytest.mark.indigo_plugin_prefs({"level": "class", "b": "class"}, merge=True)
        class TestMerged:
            def test_class(self, plugin):
                assert plugin.plugin_prefs == {"level": "class", "a": "module", "b": "class"}

            @pytest.mark.indigo_plugin_prefs({"level": "function"}, merge=True, unset=["a"])
            def test_function_merge(self, plugin):
                assert plugin.plugin_prefs == {"level": "function", "b": "class"}

            @pytest.mark.indigo_plugin_prefs({"level": "function"})
            def test_function_replace(self, plugin):
                assert plugin.plugin_prefs == {"level": "function"}
        """
    )

    pytester.runpytest().assert_outcomes(passed=4)


def test_indigo_plugin_prefs_merge_does_not_change_fixture_value(
    pytester: pytest.Pytester,
):
    make_plugin(pytester, "First")
    pytester.makepyfile(
        """
        import indigo
        import pytest

        SHARED = indigo.Dict({"key": "fixture"})

        @pytest.fixture()
        def plugin_prefs():
            return SHARED

        @pytest.mark.indigo_plugin_prefs({"key": "mark"}, merge=True)
        def test_merge(plugin):
            assert plugin.plugin_prefs == {"key": "mark"}

        def test_shared_unchanged(plugin):
            assert SHARED == {"key": "fixture"}
        """
    )

    pytester.runpytest().assert_outcomes(passed=2)


# MARK: Invalid marks
PREFS_USAGE = "Expected indigo_plugin_prefs(prefs=None, *, merge=None, unset=())"


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
            'indigo_plugin_prefs([("key", "value")])',
            "Invalid indigo_plugin_prefs mark: prefs must be a dict, but got [('key', 'value')]. "
            + PREFS_USAGE,
            id="plugin-prefs-type",
        ),
        pytest.param(
            "indigo_plugin_prefs({}, {})",
            "Invalid indigo_plugin_prefs mark: too many positional arguments. "
            + PREFS_USAGE,
            id="plugin-prefs-extra",
        ),
        pytest.param(
            "indigo_plugin_prefs({}, prefs={})",
            "Invalid indigo_plugin_prefs mark: multiple values for argument 'prefs'. "
            + PREFS_USAGE,
            id="plugin-prefs-duplicate",
        ),
        pytest.param(
            "indigo_plugin_prefs({}, replace=True)",
            "Invalid indigo_plugin_prefs mark: got an unexpected keyword argument 'replace'. "
            + PREFS_USAGE,
            id="plugin-prefs-unknown-kwarg",
        ),
        pytest.param(
            'indigo_plugin_prefs({}, merge="yes")',
            "Invalid indigo_plugin_prefs mark: merge must be a bool, but got 'yes'. "
            + PREFS_USAGE,
            id="plugin-prefs-merge-type",
        ),
        pytest.param(
            'indigo_plugin_prefs(unset="key")',
            "Invalid indigo_plugin_prefs mark: unset must be a list of str, but got 'key'. "
            + PREFS_USAGE,
            id="plugin-prefs-unset-str",
        ),
        pytest.param(
            "indigo_plugin_prefs(unset=[1])",
            "Invalid indigo_plugin_prefs mark: unset must be a list of str, but got [1]. "
            + PREFS_USAGE,
            id="plugin-prefs-unset-item-type",
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
