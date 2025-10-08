# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["AssetUpdateParams"]


class AssetUpdateParams(TypedDict, total=False):
    name: str
    """The name of the asset.

    This is shown in the Canva UI. When this field is undefined or empty, nothing is
    updated.
    """

    tags: SequenceNotStr[str]
    """
    The replacement tags for the asset. When this field is undefined, nothing is
    updated.
    """
