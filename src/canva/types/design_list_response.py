# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .design import Design
from .._models import BaseModel

__all__ = ["DesignListResponse"]


class DesignListResponse(BaseModel):
    items: List[Design]
    """The list of designs."""

    continuation: Optional[str] = None
    """
    A continuation token. If the success response contains a continuation token, the
    list contains more designs you can list. You can use this token as a query
    parameter and retrieve more designs from the list, for example
    `/v1/designs?continuation={continuation}`.

    To retrieve all of a user's designs, you might need to make multiple requests.
    """
