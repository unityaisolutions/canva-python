# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PageRetrieveParams"]


class PageRetrieveParams(TypedDict, total=False):
    limit: int
    """
    The number of pages to return, starting at the page index specified using the
    `offset` parameter.
    """

    offset: int
    """The page index to start the range of pages to return.

    Pages are indexed using one-based numbering, so the first page in a design has
    the index value `1`.
    """
