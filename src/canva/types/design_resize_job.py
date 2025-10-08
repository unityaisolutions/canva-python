# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .design_summary import DesignSummary

__all__ = ["DesignResizeJob", "Error", "Result"]


class Error(BaseModel):
    code: Literal["thumbnail_generation_error", "design_resize_error", "create_design_error", "trial_quota_exceeded"]

    message: str
    """A human-readable description of what went wrong."""


class Result(BaseModel):
    design: DesignSummary
    """Basic details about the design, such as the design's ID, title, and URL."""


class DesignResizeJob(BaseModel):
    id: str
    """The design resize job ID."""

    status: Literal["in_progress", "success", "failed"]
    """Status of the design resize job."""

    error: Optional[Error] = None
    """If the design resize job fails, this object provides details about the error."""

    result: Optional[Result] = None
    """
    Design has been created and saved to user's root
    ([projects](https://www.canva.com/help/find-designs-and-folders/)) folder.
    """
