# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .asset import Asset
from .._models import BaseModel

__all__ = ["AssetUploadJob", "Error"]


class Error(BaseModel):
    code: Literal["file_too_big", "import_failed", "fetch_failed"]
    """A short string indicating why the upload failed.

    This field can be used to handle errors programmatically.
    """

    message: str
    """A human-readable description of what went wrong."""


class AssetUploadJob(BaseModel):
    id: str
    """The ID of the asset upload job."""

    status: Literal["failed", "in_progress", "success"]
    """Status of the asset upload job."""

    asset: Optional[Asset] = None
    """The asset object, which contains metadata about the asset."""

    error: Optional[Error] = None
    """If the upload fails, this object provides details about the error."""
