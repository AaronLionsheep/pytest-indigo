import os
import sys
from collections.abc import Generator
from functools import lru_cache

from pytest import fixture

from pytest_indigo.exceptions import PytestIndigoException

from .mock import DEFAULT_API_VERSION, IndigoMock

indigo_mock = IndigoMock()
sys.modules["indigo"] = indigo_mock


@lru_cache
def find_plugin(base_dir):
    plugins = []
    for dirpath, dirnames, _ in os.walk(base_dir):
        for dirname in dirnames:
            if dirname.endswith(".indigoPlugin"):
                plugins.append(os.path.join(dirpath, dirname))

    if len(plugins) == 0:
        raise PytestIndigoException(f"No Indigo plugins were found in {base_dir}!")
    elif len(plugins) > 1:
        raise PytestIndigoException(
            "More than one Indigo plugin was found! "
            "You must manually configure pytest_indigo with the plugin to test. "
            f"{plugins}"
        )

    return plugins[0]


def pytest_addoption(parser):
    group = parser.getgroup("Indigo", "Configuration for my internal test suite")

    parser.addini(
        "indigo_api_version",
        help="Indigo Server plugin API version reported by indigo.server.apiVersion.",
        default=DEFAULT_API_VERSION,
    )

    # 2. Register the INI option fallback
    parser.addini(
        "myplugin_retries",
        help="Default retry count handled by configuration file",
        type="int",
        default=3,
    )

    # 3. Add a CLI argument to the group that overrides or complements the INI option
    group.addoption(
        "--retries",
        action="store",
        dest="cli_retries",
        help="Override the myplugin_retries INI setting via command line",
    )


@fixture(name="indigo_api_version")
def fixture_indigo_api_version(request) -> str:
    """
    Indigo Server plugin API version reported by indigo.server.apiVersion.

    Uses the indigo_api_version ini option. Override or parametrize this fixture to
    test against a different Indigo Server version.
    """
    return request.config.getini("indigo_api_version")


@fixture(name="indigo")
def fixture_indigo(indigo_api_version: str) -> Generator[IndigoMock, None, None]:
    indigo_mock.reset(api_version=indigo_api_version)
    yield indigo_mock
    indigo_mock.reset()
