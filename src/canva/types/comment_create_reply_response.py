# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .reply_comment import ReplyComment

__all__ = ["CommentCreateReplyResponse"]


class CommentCreateReplyResponse(BaseModel):
    comment: ReplyComment
    """
    Data about the reply comment, including the message, author, and the object
    (such as a design) the comment is attached to.
    """
