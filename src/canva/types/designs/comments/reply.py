# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...user import User
from ...._models import BaseModel
from .comment_content import CommentContent
from ...shared.team_user import TeamUser

__all__ = ["Reply", "Mentions"]


class Mentions(BaseModel):
    tag: str
    """The mention tag for the user mentioned in the comment thread or reply content.

    This has the format of the user's user ID and team ID separated by a colon
    (`user_id:team_id`).
    """

    user: TeamUser
    """Metadata for the user, consisting of the User ID, Team ID, and display name."""


class Reply(BaseModel):
    id: str
    """The ID of the reply."""

    content: CommentContent
    """The content of a comment thread or reply."""

    created_at: int
    """
    When the reply was created, as a Unix timestamp (in seconds since the Unix
    Epoch).
    """

    design_id: str
    """The ID of the design that the thread for this reply is attached to."""

    mentions: Dict[str, Mentions]
    """The Canva users mentioned in the comment thread or reply."""

    thread_id: str
    """The ID of the thread this reply is in."""

    updated_at: int
    """
    When the reply was last updated, as a Unix timestamp (in seconds since the Unix
    Epoch).
    """

    author: Optional[User] = None
    """Metadata for the user, consisting of the User ID and display name."""
