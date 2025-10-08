# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FolderUpdateParams"]


class FolderUpdateParams(TypedDict, total=False):
    name: Required[str]
    """The folder name, as shown in the Canva UI."""
