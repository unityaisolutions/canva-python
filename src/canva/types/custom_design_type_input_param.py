# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomDesignTypeInputParam"]


class CustomDesignTypeInputParam(TypedDict, total=False):
    height: Required[int]
    """The height of the design, in pixels."""

    type: Required[Literal["custom"]]

    width: Required[int]
    """The width of the design, in pixels."""
