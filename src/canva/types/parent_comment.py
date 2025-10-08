# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .comment_object import CommentObject
from .shared.team_user import TeamUser

__all__ = ["ParentComment"]


class ParentComment(BaseModel):
    id: str
    """The ID of the comment.

    You can use this ID to create replies to the comment using the
    [Create reply API](https://www.canva.dev/docs/connect/api-reference/comments/create-reply/).
    """

    author: User
    """Metadata for the user, consisting of the User ID and display name."""

    mentions: Dict[str, TeamUser]
    """The Canva users mentioned in the comment."""

    message: str
    """The comment message.

    This is the comment body shown in the Canva UI. User mentions are shown here in
    the format `[user_id:team_id]`.
    """

    type: Literal["parent"]

    assignee: Optional[User] = None
    """Metadata for the user, consisting of the User ID and display name."""

    attached_to: Optional[CommentObject] = None
    """If the comment is attached to a Canva Design."""

    created_at: Optional[int] = None
    """
    When the comment or reply was created, as a Unix timestamp (in seconds since the
    Unix Epoch).
    """

    resolver: Optional[User] = None
    """Metadata for the user, consisting of the User ID and display name."""

    updated_at: Optional[int] = None
    """
    When the comment or reply was last updated, as a Unix timestamp (in seconds
    since the Unix Epoch).
    """
