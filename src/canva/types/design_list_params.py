# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .sort_by_type import SortByType
from .ownership_type import OwnershipType

__all__ = ["DesignListParams"]


class DesignListParams(TypedDict, total=False):
    continuation: str
    """
    If the success response contains a continuation token, the list contains more
    designs you can list. You can use this token as a query parameter and retrieve
    more designs from the list, for example
    `/v1/designs?continuation={continuation}`.

    To retrieve all of a user's designs, you might need to make multiple requests.
    """

    ownership: OwnershipType
    """Filter the list of designs based on the user's ownership of the designs."""

    query: str
    """
    Lets you search the user's designs, and designs shared with the user, using a
    search term or terms.
    """

    sort_by: SortByType
    """Sort the list of designs."""
