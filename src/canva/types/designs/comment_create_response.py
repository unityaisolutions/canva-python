# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .thread import Thread
from ..._models import BaseModel

__all__ = ["CommentCreateResponse"]


class CommentCreateResponse(BaseModel):
    thread: Thread
    """A discussion thread on a design.

    The `type` of the thread can be found in the `thread_type` object, along with
    additional type-specific properties. The `author` of the thread might be missing
    if that user account no longer exists.
    """
