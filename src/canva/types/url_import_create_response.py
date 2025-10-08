# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .design_import_job import DesignImportJob

__all__ = ["URLImportCreateResponse"]


class URLImportCreateResponse(BaseModel):
    job: DesignImportJob
    """The status of the design import job."""
