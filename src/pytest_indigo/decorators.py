import warnings
from functools import wraps

from semver import Version

from pytest_indigo.exceptions import ApiVersionException, NotImplementedException
from pytest_indigo.warnings import PartiallyImplementedWarning


def partially_implemented(notes: str = ""):
    def _decorator(f):
        @wraps(f)
        def wrapper(*args, **kwds):
            message = (
                f"{f.__module__.removeprefix('pytest_indigo.')}.{f.__name__} "
                "has only been partially implemented by pytest-indigo! "
                f"{notes}"
            ).strip()

            warnings.warn(
                message=message,
                category=PartiallyImplementedWarning,
                stacklevel=2,
            )
            return f(*args, **kwds)

        return wrapper

    return _decorator


def not_implemented(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        raise NotImplementedException(
            f"{f.__module__.removeprefix('pytest_indigo.')}.{f.__name__} "
            "has not been implemented by pytest-indigo!"
        )

    return wrapper


def min_api_version(version: str):
    """Enforces the minimum api version required for a function"""

    def _decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            from pytest_indigo import indigo_mock as indigo

            target_version = Version.parse(
                indigo.server.apiVersion, optional_minor_and_patch=True
            )
            min_version = Version.parse(version, optional_minor_and_patch=True)
            if target_version < min_version:
                raise ApiVersionException(
                    f"The plugin is using api version {indigo.server.apiVersion}, "
                    f"but {f.__module__.removeprefix('pytest_indigo.')}.{f.__name__} "
                    f"is only present in {version} and newer!"
                )

            return f(*args, **kwargs)

        return wrapper

    return _decorator
