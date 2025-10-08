# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .thumbnail import Thumbnail

__all__ = ["Folder"]


class Folder(BaseModel):
    id: str
    """The folder ID."""

    created_at: int
    """
    When the folder was created, as a Unix timestamp (in seconds since the Unix
    Epoch).
    """

    name: str
    """The folder name."""

    updated_at: int
    """
    When the folder was last updated, as a Unix timestamp (in seconds since the Unix
    Epoch).
    """

    thumbnail: Optional[Thumbnail] = None
    """A thumbnail image representing the object."""
