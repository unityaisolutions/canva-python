# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the folder."""

    parent_folder_id: Required[str]
    """The folder ID of the parent folder.

    To create a new folder at the top level of a user's
    [projects](https://www.canva.com/help/find-designs-and-folders/), use the ID
    `root`. To create it in their Uploads folder, use `uploads`.
    """
