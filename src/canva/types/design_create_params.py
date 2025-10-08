# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .design_type_input_param import DesignTypeInputParam

__all__ = ["DesignCreateParams"]


class DesignCreateParams(TypedDict, total=False):
    asset_id: str
    """The ID of an asset to insert into the created design.

    Currently, this only supports image assets.
    """

    design_type: DesignTypeInputParam
    """The desired design type."""

    title: str
    """The name of the design."""
