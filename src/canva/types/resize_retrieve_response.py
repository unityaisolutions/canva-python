# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .design_resize_job import DesignResizeJob

__all__ = ["ResizeRetrieveResponse"]


class ResizeRetrieveResponse(BaseModel):
    job: DesignResizeJob
    """Details about the design resize job."""
