import os
import sys
from collections.abc import Generator
from functools import lru_cache

from pytest import fixture

from .mock import IndigoMock

indigo_mock = IndigoMock()
sys.modules["indigo"] = indigo_mock


class PytestIndigoException(Exception): ...


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

    return plugins


def pytest_addoption(parser):
    group = parser.getgroup("Indigo", "Configuration for my internal test suite")

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


@fixture(name="indigo")
def fixture_indigo(request) -> Generator[IndigoMock, None, None]:
    # data = request.getfixturevalue("plugin_fixture_name")
    plugins = find_plugin(request.config.rootpath)
    print(plugins)

    yield indigo_mock
    indigo_mock.reset()
