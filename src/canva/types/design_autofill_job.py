# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .design_summary import DesignSummary

__all__ = ["DesignAutofillJob", "Error", "Result"]


class Error(BaseModel):
    code: Literal["autofill_error", "thumbnail_generation_error", "create_design_error"]

    message: str
    """A human-readable description of what went wrong."""


class Result(BaseModel):
    design: DesignSummary
    """Basic details about the design, such as the design's ID, title, and URL."""

    type: Literal["create_design"]


class DesignAutofillJob(BaseModel):
    id: str
    """ID of the asynchronous job that is creating the design using the provided data."""

    status: Literal["in_progress", "success", "failed"]
    """Status of the design autofill job."""

    error: Optional[Error] = None
    """If the autofill job fails, this object provides details about the error."""

    result: Optional[Result] = None
    """Design has been created and saved to user's root folder."""
