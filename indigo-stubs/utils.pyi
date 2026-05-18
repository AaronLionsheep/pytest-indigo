"""
utils.pyi - Type stub for Py3 Libraries/utils.py.

This module is exposed as indigo.utils inside the plugin host environment.
"""

from __future__ import annotations

import json
import pathlib
from enum import Enum
from typing import TYPE_CHECKING, Any, Final

if TYPE_CHECKING:
    import indigo

# ---------------------------------------------------------------------------
# JSON encoding
# ---------------------------------------------------------------------------

class JSONDateEncoder(json.JSONEncoder):
    """JSON encoder that converts datetime/date to ISO strings and NaN to None.
    Also converts Indigo constant objects to their full specifier string
    (e.g. 'indigo.kFanMode.Auto').
    """
    def default(self, obj: object) -> object: ...


IndigoJSONEncoder = JSONDateEncoder
"""Alias for JSONDateEncoder."""


# ---------------------------------------------------------------------------
# Boolean string helpers
# ---------------------------------------------------------------------------

BOOL_MAP_TRUE: dict[str, str]
"""Maps truthy string values to their opposite falsy strings."""

BOOL_MAP_FALSE: dict[str, str]
"""Maps falsy string values to their opposite truthy strings."""


def is_int(value: Any) -> bool:
    """Return True if *value* is an integer or can be cast to one."""
    ...


def str_to_bool(val: str) -> bool:
    """Convert a string representation of truth ('yes', 'true', 'on', '1', 'open',
    'locked', …) to bool. Raises ValueError for unrecognised values."""
    ...


def reverse_bool_str_value(val: str) -> str:
    """Return the opposite boolean string value (e.g. 'on' → 'off', 'yes' → 'no')."""
    ...


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

class ValidationError(Exception):
    """Exception for field-level validation failures.

    Contains an optional error_dict mapping field names to error message(s),
    and an optional error_state_str for device-state errors.
    """

    error_message: str
    error_state_str: str | None
    error_dict: dict

    def __init__(
        self,
        message: str,
        error_state_str: str | None = None,
        error_dict: dict | None = None,
    ) -> None: ...

    def add_error(self, key: str, description: str | list) -> None:
        """Add one or more error messages for *key* to error_dict."""
        ...

    def remove_error(self, key: str) -> str | list | None:
        """Remove all error messages for *key* from error_dict and return them."""
        ...

    def raise_if_errors(self) -> None:
        """Raise self if error_dict is non-empty or error_state_str is set."""
        ...

    def __iter__(self): ...


# ---------------------------------------------------------------------------
# Email validation
# ---------------------------------------------------------------------------

def validate_email_address(address: str) -> bool:
    """Return True if *address* looks like a valid email address."""
    ...


# ---------------------------------------------------------------------------
# Control-page geometry helpers
# ---------------------------------------------------------------------------

class Size:
    """Width/height pair."""
    width: int
    height: int
    def __init__(self, width: int, height: int) -> None: ...


class Point:
    """X/Y coordinate pair."""
    x: int
    y: int
    def __init__(self, x: int, y: int) -> None: ...


class RGBColor:
    """RGB colour represented as two-character hex strings per channel.

    Construct with either a 6-character hex string or explicit r/g/b hex pairs.
    """
    red: str
    green: str
    blue: str

    def __init__(
        self,
        hex_str: str | None = None,
        red: str | None = None,
        green: str | None = None,
        blue: str | None = None,
    ) -> None: ...

    def __str__(self) -> str: ...


# ---------------------------------------------------------------------------
# Control-page enumerations
# ---------------------------------------------------------------------------

class ControlPageBaseEnum(Enum):
    """Base enum whose __str__ returns 'indigo.utils.<Class>.<member>'."""
    def __str__(self) -> str: ...


class CaptionPlacementEnum(ControlPageBaseEnum):
    CENTER_ABOVE_IMAGE: CaptionPlacementEnum
    CENTER_ON_IMAGE: CaptionPlacementEnum
    CENTER_BELOW_IMAGE: CaptionPlacementEnum
    LEFT_OF_IMAGE: CaptionPlacementEnum
    RIGHT_OF_IMAGE: CaptionPlacementEnum


class PageElementTypeEnum(ControlPageBaseEnum):
    NONE: PageElementTypeEnum
    DEVICE_CONTROL: PageElementTypeEnum
    VARIABLE_CONTROL: PageElementTypeEnum
    VIDEO_CONTROL: PageElementTypeEnum
    ACTION_GROUP_CONTROL: PageElementTypeEnum
    CONTROL_PAGE_CONTROL: PageElementTypeEnum
    FOLDER_FILTER_CONTROL: PageElementTypeEnum
    IMAGE_TEXT_CONTROL: PageElementTypeEnum
    REFRESHING_IMAGE_CONTROL: PageElementTypeEnum
    SERVER_STATUS_CONTROL: PageElementTypeEnum
    SERVER_ICON_CONTROL: PageElementTypeEnum


class TextAlignmentTypeEnum(ControlPageBaseEnum):
    LEFT: TextAlignmentTypeEnum
    RIGHT: TextAlignmentTypeEnum
    CENTER: TextAlignmentTypeEnum


class FontTypeEnum(ControlPageBaseEnum):
    ARIAL: FontTypeEnum
    ARIAL_BLACK: FontTypeEnum
    VERDANA: FontTypeEnum
    IMPACT: FontTypeEnum
    LATO_LIGHT: FontTypeEnum
    LATO_LIGHT_ITALIC: FontTypeEnum
    LATO_MEDIUM: FontTypeEnum
    LATO_MEDIUM_ITALIC: FontTypeEnum
    LATO_HEAVY: FontTypeEnum
    LATO_HEAVY_ITALIC: FontTypeEnum
    GEORGIA: FontTypeEnum
    TIMES_NEW_ROMAN: FontTypeEnum
    COURIER_NEW: FontTypeEnum
    MONOCO_NEW: FontTypeEnum
    COMIC_SANS: FontTypeEnum

    @property
    def as_css_string(self) -> str:
        """Return the CSS font-family string for this font."""
        ...


class ClientActionTypeEnum(Enum):
    NONE: ClientActionTypeEnum
    POPUP_CONTROLS: ClientActionTypeEnum
    LINK_TO_CONTROL_PAGE_NAVIGATE: ClientActionTypeEnum
    EXTERNAL_URL: ClientActionTypeEnum
    CONTROL_PAGE_REPLACE: ClientActionTypeEnum
    PREVIOUS_PAGE: ClientActionTypeEnum
    CONTROL_PAGE_LIST: ClientActionTypeEnum


class ServerActionClassEnum(Enum):
    BASE: ServerActionClassEnum
    CONTROL_DEVICES: ServerActionClassEnum
    CONTROL_SPRINKLER: ServerActionClassEnum
    CONTROL_THERMOSTAT: ServerActionClassEnum
    CONTROL_IO: ServerActionClassEnum
    CONTROL_IR: ServerActionClassEnum
    CONTROL_VIDEO: ServerActionClassEnum
    CONTROL_SPEED_CONTROL: ServerActionClassEnum
    CONTROL_SENSOR: ServerActionClassEnum
    CONTROL_GENERAL: ServerActionClassEnum
    EXECUTE_GROUP: ServerActionClassEnum
    EXECUTE_SCRIPT: ServerActionClassEnum
    EXECUTE_SCENE: ServerActionClassEnum
    ENABLE_DISABLE: ServerActionClassEnum
    MODIFY_VARIABLE: ServerActionClassEnum
    REMOVE_DELAYED_ACTIONS: ServerActionClassEnum
    SEND_EMAIL: ServerActionClassEnum
    RESET_INTERFACE_CONN: ServerActionClassEnum
    PLUGIN: ServerActionClassEnum
    IS_MULTIPLE: ServerActionClassEnum


# ---------------------------------------------------------------------------
# Control-page element and detail page
# ---------------------------------------------------------------------------

class PageElement:
    """A single element (widget) on an Indigo control page."""

    element_type: PageElementTypeEnum
    position: Point
    size: Size
    caption_name: str
    caption_placement: CaptionPlacementEnum
    caption_font_type: FontTypeEnum
    caption_font_color: RGBColor
    caption_font_size: int
    caption_current_size: Size
    caption_wraps: bool
    caption_pos_style: str
    show_state_image: bool
    show_state_text: bool
    state_text_alignment: TextAlignmentTypeEnum
    state_text_font: FontTypeEnum
    state_text_font_color: RGBColor
    state_text_font_size: int
    image_filename: str | None
    image_file_url: str | None
    image_filename_needs_resolver: bool
    image_refresh_duration: int
    target_elem_id: int | None
    target_elem_name: str | None
    target_elem_sub_key: str | None
    value_long: str | None
    value_raw: str | None
    control_index: int
    client_action_type: ClientActionTypeEnum
    server_action_class: ServerActionClassEnum
    action_link_target: int | None
    action_link_target_id: int | None
    action_link_opens_new_window: bool
    action_link_href_target: str
    popup_control_path: str | None

    def __init__(self, raw_pe: "indigo.Dict", base_image_path: str | pathlib.Path) -> None: ...


class DetailControlPage:
    """An indigo.ControlPage enriched with full layout details (page elements)."""

    id: int
    name: str
    description: str
    folder_id: int
    hide_tab_bar: bool
    remote_display: bool
    background_image: object
    background_color: RGBColor
    size: Size
    change_count: int
    global_props: "indigo.Dict"
    plugin_props: "indigo.Dict"
    shared_props: "indigo.Dict"
    page_element_list: list[PageElement]
    page_element_errors: list[Exception]

    def __init__(
        self,
        base_image_path: str | pathlib.Path,
        cp_id: int | str | None = None,
        cp_instance: "indigo.ControlPage" | None = None,
    ) -> None: ...


# ---------------------------------------------------------------------------
# Image path resolution
# ---------------------------------------------------------------------------

def image_file_exists(base_path: pathlib.Path, url_path: pathlib.Path) -> bool:
    """Return True if *base_path* / *url_path* exists on disk."""
    ...


def get_image_path_simple(
    control_type: PageElementTypeEnum,
    name: str | None,
    value: Any | None,
    filename: str,
    base_image_path: str | pathlib.Path,
) -> str:
    """Return the best matching image URL path for binary (on/off) images."""
    ...


def get_image_path_with_resolver(
    control_type: PageElementTypeEnum,
    name: str | None,
    value: Any | None,
    filename: str,
    base_image_path: str | pathlib.Path,
) -> str:
    """Return the best matching image URL path using multi-step resolution heuristics."""
    ...


# ---------------------------------------------------------------------------
# Web server file streaming helper
# ---------------------------------------------------------------------------

FILE_EXTENSION_MIME_MAP: Final[dict[str, str]]
"""Maps common file extensions to MIME type strings."""


def return_static_file(
    file_path: str | list,
    status: int = 200,
    path_is_relative: bool = True,
    content_type: str | None = None,
) -> "indigo.Dict":
    """Return an indigo.Dict that instructs the Indigo Web Server to stream *file_path*
    back to the HTTP caller."""
    ...


# ---------------------------------------------------------------------------
# Control-page flag helpers
# ---------------------------------------------------------------------------

CAPTION_BUFFER_SPACE: Final[int]
"""Pixel gap between a caption and its state image (must match Indigo page editor)."""

FULL_PAGE_FLAGS: Final[int]
"""Pre-computed flag value for retrieving a full control page."""

PAGE_STATUS_FLAGS: Final[int]
"""Pre-computed flag value for retrieving control page status only."""


def calc_getPage_flags(
    ignore_page_elems: int,
    ignore_actions: int,
    retrieve_as_list: int,
    embed_control_target_elems: int,
) -> int:
    """Compute the GetControlPage flags bitmask from individual boolean options."""
    ...


def get_next_integer_step(integer: int, step: int) -> int:
    """Round *integer* to the nearest multiple of *step*."""
    ...


# ---------------------------------------------------------------------------
# Shared module loader
# ---------------------------------------------------------------------------

def get_shared_module_list() -> list:
    """Return the list of shared Python modules available in the Python-includes folder."""
    ...
