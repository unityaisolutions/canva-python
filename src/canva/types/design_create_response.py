# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .design import Design
from .._models import BaseModel

__all__ = ["DesignCreateResponse"]


class DesignCreateResponse(BaseModel):
    design: Design
    """The design object, which contains metadata about the design."""
