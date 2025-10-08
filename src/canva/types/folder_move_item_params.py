# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FolderMoveItemParams"]


class FolderMoveItemParams(TypedDict, total=False):
    item_id: Required[str]
    """The ID of the item you want to move. Currently, video assets are not supported."""

    to_folder_id: Required[str]
    """
    The ID of the folder you want to move the item to (the destination folder). If
    you want to move the item to the top level of a Canva user's
    [projects](https://www.canva.com/help/find-designs-and-folders/), use the ID
    `root`.
    """
