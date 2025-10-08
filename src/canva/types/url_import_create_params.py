# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLImportCreateParams"]


class URLImportCreateParams(TypedDict, total=False):
    title: Required[str]
    """A title for the design."""

    url: Required[str]
    """The URL of the file to import.

    This URL must be accessible from the internet and be publicly available.
    """

    mime_type: str
    """The MIME type of the file being imported.

    If not provided, Canva attempts to automatically detect the type of the file.
    """
