# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Thumbnail"]


class Thumbnail(BaseModel):
    height: int
    """The height of the thumbnail image in pixels."""

    url: str
    """A URL for retrieving the thumbnail image. This URL expires after 15 minutes.

    This URL includes a query string that's required for retrieving the thumbnail.
    """

    width: int
    """The width of the thumbnail image in pixels."""
