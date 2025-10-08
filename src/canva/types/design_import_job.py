# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .design_summary import DesignSummary

__all__ = ["DesignImportJob", "Error", "Result"]


class Error(BaseModel):
    code: Literal[
        "design_creation_throttled",
        "design_import_throttled",
        "duplicate_import",
        "internal_error",
        "invalid_file",
        "fetch_failed",
    ]
    """A short string about why the import failed.

    This field can be used to handle errors programmatically.
    """

    message: str
    """A human-readable description of what went wrong."""


class Result(BaseModel):
    designs: List[DesignSummary]
    """A list of designs imported from the external file.

    It usually contains one item. Imports with a large number of pages or assets are
    split into multiple designs.
    """


class DesignImportJob(BaseModel):
    id: str
    """The ID of the design import job."""

    status: Literal["failed", "in_progress", "success"]
    """The status of the design import job."""

    error: Optional[Error] = None
    """If the import job fails, this object provides details about the error."""

    result: Optional[Result] = None
