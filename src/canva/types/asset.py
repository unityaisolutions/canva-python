# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .thumbnail import Thumbnail
from .asset_type import AssetType
from .users.team_user_summary import TeamUserSummary

__all__ = ["Asset", "ImportStatus", "ImportStatusError"]


class ImportStatusError(BaseModel):
    code: Literal["file_too_big", "import_failed"]
    """A short string indicating why the upload failed.

    This field can be used to handle errors programmatically.
    """

    message: str
    """A human-readable description of what went wrong."""


class ImportStatus(BaseModel):
    state: Literal["failed", "in_progress", "success"]
    """State of the import job for an uploaded asset."""

    error: Optional[ImportStatusError] = None
    """If the import fails, this object provides details about the error."""


class Asset(BaseModel):
    id: str
    """The ID of the asset."""

    created_at: int
    """
    When the asset was added to Canva, as a Unix timestamp (in seconds since the
    Unix Epoch).
    """

    name: str
    """The name of the asset."""

    owner: TeamUserSummary
    """Metadata for the user, consisting of the User ID and Team ID."""

    tags: List[str]
    """
    The user-facing tags attached to the asset. Users can add these tags to their
    uploaded assets, and they can search their uploaded assets in the Canva UI by
    searching for these tags. For information on how users use tags, see the
    [Canva Help Center page on asset tags](https://www.canva.com/help/add-edit-tags/).
    """

    type: AssetType
    """Type of an asset."""

    updated_at: int
    """
    When the asset was last updated in Canva, as a Unix timestamp (in seconds since
    the Unix Epoch).
    """

    import_status: Optional[ImportStatus] = None
    """The import status of the asset."""

    thumbnail: Optional[Thumbnail] = None
    """A thumbnail image representing the object."""
