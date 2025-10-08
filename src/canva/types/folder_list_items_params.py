# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["FolderListItemsParams"]


class FolderListItemsParams(TypedDict, total=False):
    continuation: str
    """
    If the success response contains a continuation token, the folder contains more
    items you can list. You can use this token as a query parameter and retrieve
    more items from the list, for example
    `/v1/folders/{folderId}/items?continuation={continuation}`.

    To retrieve all the items in a folder, you might need to make multiple requests.
    """

    item_types: List[Literal["design", "folder", "image"]]
    """Filter the folder items to only return specified types.

    The available types are: `design`, `folder`, and `image`. To filter for more
    than one item type, provide a comma- delimited list.
    """

    sort_by: Literal[
        "created_ascending",
        "created_descending",
        "modified_ascending",
        "modified_descending",
        "title_ascending",
        "title_descending",
    ]
    """Sort the list of folder items.

    - `created_ascending` - Sort results by creation date, in ascending order.
    - `created_descending` - Sort results by creation date, in descending order.
    - `modified_ascending` - Sort results by the last modified date, in ascending
      order.
    - `modified_descending` - Sort results by the last modified date, in descending
      order.
    - `title_ascending` - Sort results by title, in ascending order. The title is
      either the `name` field for a folder or asset, or the `title` field for a
      design.
    - `title_descending` - Sort results by title, in descending order. The title is
      either the `name` field for a folder or asset, or the `title` field for a
      design.
    """
