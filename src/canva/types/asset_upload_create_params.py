# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetUploadCreateParams"]


class AssetUploadCreateParams(TypedDict, total=False):
    asset_upload_metadata: Required[Annotated[object, PropertyInfo(alias="Asset-Upload-Metadata")]]
