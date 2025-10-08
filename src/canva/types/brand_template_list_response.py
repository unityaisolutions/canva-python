# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .brand_template import BrandTemplate

__all__ = ["BrandTemplateListResponse"]


class BrandTemplateListResponse(BaseModel):
    items: List[BrandTemplate]
    """The list of brand templates."""

    continuation: Optional[str] = None
    """
    If the success response contains a continuation token, the user has access to
    more brand templates you can list. You can use this token as a query parameter
    and retrieve more templates from the list, for example
    `/v1/brand-templates?continuation={continuation}`. To retrieve all the brand
    templates available to the user, you might need to make multiple requests.
    """
