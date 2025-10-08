# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .parent_comment import ParentComment

__all__ = ["CommentCreateThreadResponse"]


class CommentCreateThreadResponse(BaseModel):
    comment: ParentComment
    """
    Data about the comment, including the message, author, and the object (such as a
    design) the comment is attached to.
    """
