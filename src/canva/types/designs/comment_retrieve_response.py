# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Annotated, TypeAlias

from .thread import Thread
from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..reply_comment import ReplyComment
from ..parent_comment import ParentComment

__all__ = ["CommentRetrieveResponse", "Comment"]

Comment: TypeAlias = Annotated[Union[ParentComment, ReplyComment], PropertyInfo(discriminator="type")]


class CommentRetrieveResponse(BaseModel):
    comment: Optional[Comment] = None
    """
    The comment object, which contains metadata about the comment. Deprecated in
    favor of the new `thread` object.
    """

    thread: Optional[Thread] = None
    """A discussion thread on a design.

    The `type` of the thread can be found in the `thread_type` object, along with
    additional type-specific properties. The `author` of the thread might be missing
    if that user account no longer exists.
    """
