# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReplyListParams"]


class ReplyListParams(TypedDict, total=False):
    design_id: Required[Annotated[str, PropertyInfo(alias="designId")]]

    continuation: str
    """
    If the success response contains a continuation token, the list contains more
    items you can list. You can use this token as a query parameter and retrieve
    more items from the list, for example `?continuation={continuation}`.

    To retrieve all items, you might need to make multiple requests.
    """

    limit: int
    """The number of replies to return."""
