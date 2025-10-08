# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .export_quality import ExportQuality

__all__ = [
    "ExportCreateParams",
    "Format",
    "FormatPdfExportFormat",
    "FormatJpgExportFormat",
    "FormatPngExportFormat",
    "FormatPptxExportFormat",
    "FormatGifExportFormat",
    "FormatMP4ExportFormat",
]


class ExportCreateParams(TypedDict, total=False):
    design_id: Required[str]
    """The design ID."""

    format: Required[Format]
    """Details about the desired export format."""


class FormatPdfExportFormat(TypedDict, total=False):
    type: Required[Literal["pdf"]]

    export_quality: ExportQuality
    """Specifies the export quality of the design."""

    pages: Iterable[int]
    """
    To specify which pages to export in a multi-page design, provide the page
    numbers as an array. The first page in a design is page `1`. If `pages` isn't
    specified, all the pages are exported.
    """

    size: Literal["a4", "a3", "letter", "legal"]
    """The paper size of the export PDF file.

    The `size` attribute is only supported for Documents (Canva Docs).
    """


class FormatJpgExportFormat(TypedDict, total=False):
    quality: Required[int]
    """
    For the `jpg` type, the `quality` of the exported JPEG determines how compressed
    the exported file should be. A _low_ `quality` value will create a file with a
    smaller file size, but the resulting file will have pixelated artifacts when
    compared to a file created with a _high_ `quality` value.
    """

    type: Required[Literal["jpg"]]

    export_quality: ExportQuality
    """Specifies the export quality of the design."""

    height: int
    """Specify the height in pixels of the exported image. Note the following behavior:

    - If no height or width is specified, the image is exported using the dimensions
      of the design.
    - If only one of height or width is specified, then the image is scaled to match
      that dimension, respecting the design's aspect ratio.
    - If both the height and width are specified, but the values don't match the
      design's aspect ratio, the export defaults to the larger dimension.
    """

    pages: Iterable[int]
    """
    To specify which pages to export in a multi-page design, provide the page
    numbers as an array. The first page in a design is page `1`. If `pages` isn't
    specified, all the pages are exported.
    """

    width: int
    """Specify the width in pixels of the exported image. Note the following behavior:

    - If no width or height is specified, the image is exported using the dimensions
      of the design.
    - If only one of width or height is specified, then the image is scaled to match
      that dimension, respecting the design's aspect ratio.
    - If both the width and height are specified, but the values don't match the
      design's aspect ratio, the export defaults to the larger dimension.
    """


class FormatPngExportFormat(TypedDict, total=False):
    type: Required[Literal["png"]]

    as_single_image: bool
    """
    When `true`, multi-page designs are merged into a single image. When `false`
    (default), each page is exported as a separate image.
    """

    export_quality: ExportQuality
    """Specifies the export quality of the design."""

    height: int
    """Specify the height in pixels of the exported image. Note the following behavior:

    - If no height or width is specified, the image is exported using the dimensions
      of the design.
    - If only one of height or width is specified, then the image is scaled to match
      that dimension, respecting the design's aspect ratio.
    - If both the height and width are specified, but the values don't match the
      design's aspect ratio, the export defaults to the larger dimension.
    """

    lossless: bool
    """
    If set to `true` (default), the PNG is exported without compression. If set to
    `false`, the PNG is compressed using a lossy compression algorithm. Lossy PNG
    compression is only available to users on a Canva plan that has premium
    features, such as Canva Pro. If the user is on the Canva Free plan and this
    parameter is set to `false`, the export operation will fail.
    """

    pages: Iterable[int]
    """
    To specify which pages to export in a multi-page design, provide the page
    numbers as an array. The first page in a design is page `1`. If `pages` isn't
    specified, all the pages are exported.
    """

    transparent_background: bool
    """
    If set to `true`, the PNG is exported with a transparent background. This option
    is only available to users on a Canva plan that has premium features, such as
    Canva Pro. If the user is on the Canva Free plan and this parameter is set to
    `true`, the export operation will fail.
    """

    width: int
    """Specify the width in pixels of the exported image. Note the following behavior:

    - If no width or height is specified, the image is exported using the dimensions
      of the design.
    - If only one of width or height is specified, then the image is scaled to match
      that dimension, respecting the design's aspect ratio.
    - If both the width and height are specified, but the values don't match the
      design's aspect ratio, the export defaults to the larger dimension.
    """


class FormatPptxExportFormat(TypedDict, total=False):
    type: Required[Literal["pptx"]]

    pages: Iterable[int]
    """
    To specify which pages to export in a multi-page design, provide the page
    numbers as an array. The first page in a design is page `1`. If `pages` isn't
    specified, all the pages are exported.
    """


class FormatGifExportFormat(TypedDict, total=False):
    type: Required[Literal["gif"]]

    export_quality: ExportQuality
    """Specifies the export quality of the design."""

    height: int
    """Specify the height in pixels of the exported image. Note the following behavior:

    - If no height or width is specified, the image is exported using the dimensions
      of the design.
    - If only one of height or width is specified, then the image is scaled to match
      that dimension, respecting the design's aspect ratio.
    - If both the height and width are specified, but the values don't match the
      design's aspect ratio, the export defaults to the larger dimension.
    """

    pages: Iterable[int]
    """
    To specify which pages to export in a multi-page design, provide the page
    numbers as an array. The first page in a design is page `1`. If `pages` isn't
    specified, all the pages are exported.
    """

    width: int
    """Specify the width in pixels of the exported image. Note the following behavior:

    - If no width or height is specified, the image is exported using the dimensions
      of the design.
    - If only one of width or height is specified, then the image is scaled to match
      that dimension, respecting the design's aspect ratio.
    - If both the width and height are specified, but the values don't match the
      design's aspect ratio, the export defaults to the larger dimension.
    """


class FormatMP4ExportFormat(TypedDict, total=False):
    quality: Required[
        Literal[
            "horizontal_480p",
            "horizontal_720p",
            "horizontal_1080p",
            "horizontal_4k",
            "vertical_480p",
            "vertical_720p",
            "vertical_1080p",
            "vertical_4k",
        ]
    ]
    """The orientation and resolution of the exported video.

    Orientation is either `horizontal` or `vertical`, and resolution is one of
    `480p`, `720p`, `1080p` or `4k`.
    """

    type: Required[Literal["mp4"]]

    export_quality: ExportQuality
    """Specifies the export quality of the design."""

    pages: Iterable[int]
    """
    To specify which pages to export in a multi-page design, provide the page
    numbers as an array. The first page in a design is page `1`. If `pages` isn't
    specified, all the pages are exported.
    """


Format: TypeAlias = Union[
    FormatPdfExportFormat,
    FormatJpgExportFormat,
    FormatPngExportFormat,
    FormatPptxExportFormat,
    FormatGifExportFormat,
    FormatMP4ExportFormat,
]
