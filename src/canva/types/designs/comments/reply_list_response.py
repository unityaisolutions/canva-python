# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .reply import Reply
from ...._models import BaseModel

__all__ = ["ReplyListResponse"]


class ReplyListResponse(BaseModel):
    items: List[Reply]

    continuation: Optional[str] = None
    """
    If the success response contains a continuation token, the list contains more
    items you can list. You can use this token as a query parameter and retrieve
    more items from the list, for example `?continuation={continuation}`.

    To retrieve all items, you might need to make multiple requests.
    """
