# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .design_type_input_param import DesignTypeInputParam

__all__ = ["ResizeCreateParams"]


class ResizeCreateParams(TypedDict, total=False):
    design_id: Required[str]
    """The design ID."""

    design_type: Required[DesignTypeInputParam]
    """The desired design type."""
