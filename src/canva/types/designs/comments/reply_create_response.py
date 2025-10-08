# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .reply import Reply
from ...._models import BaseModel

__all__ = ["ReplyCreateResponse"]


class ReplyCreateResponse(BaseModel):
    reply: Reply
    """A reply to a thread.

    The `author` of the reply might be missing if that user account no longer
    exists.
    """
