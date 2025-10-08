# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExportFormatRetrieveResponse", "Formats"]


class Formats(BaseModel):
    gif: Optional[object] = None
    """Whether the design can be exported as a GIF."""

    jpg: Optional[object] = None
    """Whether the design can be exported as a JPEG."""

    mp4: Optional[object] = None
    """Whether the design can be exported as an MP4."""

    pdf: Optional[object] = None
    """Whether the design can be exported as a PDF."""

    png: Optional[object] = None
    """Whether the design can be exported as a PNG."""

    pptx: Optional[object] = None
    """Whether the design can be exported as a PPTX."""

    svg: Optional[object] = None
    """Whether the design can be exported as an SVG."""


class ExportFormatRetrieveResponse(BaseModel):
    formats: Formats
    """The available file formats for exporting the design."""
