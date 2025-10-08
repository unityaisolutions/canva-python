# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..thumbnail import Thumbnail

__all__ = ["PageRetrieveResponse", "Item"]


class Item(BaseModel):
    index: int
    """The index of the page in the design.

    The first page in a design has the index value `1`.
    """

    thumbnail: Optional[Thumbnail] = None
    """A thumbnail image representing the object."""


class PageRetrieveResponse(BaseModel):
    items: List[Item]
    """The list of pages."""
