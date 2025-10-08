# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["CommentContent"]


class CommentContent(BaseModel):
    plaintext: str
    """
    The content in plaintext. Any user mention tags are shown in the format
    `[user_id:team_id]`.
    """

    markdown: Optional[str] = None
    """
    The content in markdown. Any user mention tags are shown in the format
    `[user_id:team_id]`
    """
