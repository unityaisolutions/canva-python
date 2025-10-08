# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .thumbnail import Thumbnail
from .design_links import DesignLinks
from .users.team_user_summary import TeamUserSummary

__all__ = ["Design"]


class Design(BaseModel):
    id: str
    """The design ID."""

    created_at: int
    """
    When the design was created in Canva, as a Unix timestamp (in seconds since the
    Unix Epoch).
    """

    owner: TeamUserSummary
    """Metadata for the user, consisting of the User ID and Team ID."""

    updated_at: int
    """
    When the design was last updated in Canva, as a Unix timestamp (in seconds since
    the Unix Epoch).
    """

    urls: DesignLinks
    """A temporary set of URLs for viewing or editing the design."""

    page_count: Optional[int] = None
    """The total number of pages in the design.

    Some design types don't have pages (for example, Canva docs).
    """

    thumbnail: Optional[Thumbnail] = None
    """A thumbnail image representing the object."""

    title: Optional[str] = None
    """The design title."""
