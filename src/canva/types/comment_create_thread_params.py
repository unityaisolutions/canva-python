# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .comment_object_input_param import CommentObjectInputParam

__all__ = ["CommentCreateThreadParams"]


class CommentCreateThreadParams(TypedDict, total=False):
    attached_to: Required[CommentObjectInputParam]
    """If the comment is attached to a Canva Design."""

    message: Required[str]
    """The comment message. This is the comment body shown in the Canva UI.

    You can also mention users in your message by specifying their User ID and Team
    ID using the format `[user_id:team_id]`. If the `assignee_id` parameter is
    specified, you must mention the assignee in the message.
    """

    assignee_id: str
    """Lets you assign the comment to a Canva user using their User ID.

    You _must_ mention the assigned user in the `message`.
    """
