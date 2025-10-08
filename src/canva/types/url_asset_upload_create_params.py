# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLAssetUploadCreateParams"]


class URLAssetUploadCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for the asset."""

    url: Required[str]
    """The URL of the file to import.

    This URL must be accessible from the internet and be publicly available.
    """
