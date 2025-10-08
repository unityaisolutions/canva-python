# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .brand_template import BrandTemplate

__all__ = ["BrandTemplateRetrieveResponse"]


class BrandTemplateRetrieveResponse(BaseModel):
    brand_template: BrandTemplate
    """An object representing a brand template with associated metadata."""
