import os

import pytest

from pytest_indigo import PytestIndigoException, find_plugin


def test_find_plugin_raises_exception_with_multiple_plugins(request):
    with pytest.raises(
        PytestIndigoException, match="More than one Indigo plugin was found!"
    ):
        find_plugin(os.path.join(request.config.rootpath, "integration"))


def test_find_plugin_raises_exception_with_no_plugins(request):
    dir = os.path.join(request.config.rootpath, "src")
    with pytest.raises(
        PytestIndigoException, match=f"No Indigo plugins were found in {dir}"
    ):
        find_plugin(dir)


def test_find_plugin(request):
    dir = os.path.join(request.config.rootpath, "integration/basic")
    assert find_plugin(dir) == os.path.join(dir, "Basic.indigoPlugin")
