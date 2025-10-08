# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .thumbnail import Thumbnail

__all__ = ["BrandTemplate"]


class BrandTemplate(BaseModel):
    id: str
    """The brand template ID."""

    create_url: str
    """A URL Canva users can visit to create a new design from the template."""

    created_at: int
    """
    When the brand template was created, as a Unix timestamp (in seconds since the
    Unix Epoch).
    """

    title: str
    """The brand template title, as shown in the Canva UI."""

    updated_at: int
    """
    When the brand template was last updated, as a Unix timestamp (in seconds since
    the Unix Epoch).
    """

    view_url: str
    """A URL Canva users can visit to view the brand template."""

    thumbnail: Optional[Thumbnail] = None
    """A thumbnail image representing the object."""
