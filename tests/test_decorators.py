import pytest

from pytest_indigo import IndigoMock
from pytest_indigo.decorators import (
    min_api_version,
    not_implemented,
    partially_implemented,
)
from pytest_indigo.exceptions import ApiVersionException, NotImplementedException
from pytest_indigo.warnings import PartiallyImplementedWarning


# MARK: partially_implemented()
class TestPartiallyImplemented:
    def test_returns_result(self):
        @partially_implemented()
        def func(a, b=0):
            return a + b

        with pytest.warns(PartiallyImplementedWarning):
            assert func(1, b=2) == 3

    def test_message_with_notes(self):
        @partially_implemented("Some notes.")
        def func():
            pass

        with pytest.warns(
            PartiallyImplementedWarning,
            match=r"^tests\.test_decorators\.func has only been partially implemented by pytest-indigo! Some notes\.$",
        ):
            func()

    def test_message_without_notes(self):
        @partially_implemented()
        def func():
            pass

        with pytest.warns(
            PartiallyImplementedWarning,
            match=r"^tests\.test_decorators\.func has only been partially implemented by pytest-indigo!$",
        ):
            func()

    def test_strips_package_prefix(self, indigo: IndigoMock):
        with pytest.warns(
            PartiallyImplementedWarning, match=r"^indigo\.server\.getPluginList "
        ):
            indigo.server.getPluginList()

    def test_warning_points_at_caller(self):
        @partially_implemented()
        def func():
            pass

        with pytest.warns(PartiallyImplementedWarning) as record:
            func()

        assert record[0].filename == __file__

    def test_preserves_metadata(self):
        @partially_implemented()
        def func():
            """Docstring."""

        assert func.__name__ == "func"
        assert func.__doc__ == "Docstring."


# MARK: not_implemented()
class TestNotImplemented:
    def test_raises(self):
        @not_implemented
        def func():
            return "result"

        with pytest.raises(
            NotImplementedException,
            match=r"^tests\.test_decorators\.func has not been implemented by pytest-indigo!$",
        ):
            func()

    def test_does_not_call_function(self):
        calls = []

        @not_implemented
        def func():
            calls.append(True)

        with pytest.raises(NotImplementedException):
            func()

        assert calls == []

    def test_accepts_any_arguments(self):
        @not_implemented
        def func(a):
            pass

        with pytest.raises(NotImplementedException):
            func(1, 2, key="value")

    def test_preserves_metadata(self):
        @not_implemented
        def func():
            """Docstring."""

        assert func.__name__ == "func"
        assert func.__doc__ == "Docstring."


# MARK: min_api_version()
class TestMinApiVersion:
    @pytest.mark.parametrize(
        ("indigo_api_version", "min_version"),
        [
            pytest.param("2.4", "2.4", id="equal"),
            pytest.param("3", "2.4", id="newer-major"),
            pytest.param("2.5", "2.4", id="newer-minor"),
            pytest.param("3.0.1", "3", id="newer-patch"),
            pytest.param("3", "3.0.0", id="optional-minor-and-patch"),
        ],
    )
    def test_supported(self, indigo: IndigoMock, min_version):
        @min_api_version(min_version)
        def func(a, b=0):
            return a + b

        assert func(1, b=2) == 3

    @pytest.mark.parametrize(
        ("indigo_api_version", "min_version"),
        [
            pytest.param("1.8", "2.4", id="older-major"),
            pytest.param("2.3", "2.4", id="older-minor"),
            pytest.param("3", "3.0.1", id="older-patch"),
        ],
    )
    def test_unsupported(self, indigo: IndigoMock, indigo_api_version, min_version):
        @min_api_version(min_version)
        def func():
            pass

        with pytest.raises(
            ApiVersionException,
            match=(
                rf"^The plugin is using api version {indigo_api_version}, "
                rf"but tests\.test_decorators\.func is only present in {min_version} and newer!$"
            ),
        ):
            func()

    @pytest.mark.parametrize("indigo_api_version", ["1.8"])
    def test_does_not_call_function_when_unsupported(self, indigo: IndigoMock):
        calls = []

        @min_api_version("2.4")
        def func():
            calls.append(True)

        with pytest.raises(ApiVersionException):
            func()

        assert calls == []

    def test_preserves_metadata(self):
        @min_api_version("2.4")
        def func():
            """Docstring."""

        assert func.__name__ == "func"
        assert func.__doc__ == "Docstring."
