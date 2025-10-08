# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .export_job import ExportJob

__all__ = ["ExportRetrieveResponse"]


class ExportRetrieveResponse(BaseModel):
    job: ExportJob
    """The status of the export job."""
