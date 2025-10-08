# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .design_autofill_job import DesignAutofillJob

__all__ = ["AutofillCreateResponse"]


class AutofillCreateResponse(BaseModel):
    job: DesignAutofillJob
    """Details about the autofill job."""
