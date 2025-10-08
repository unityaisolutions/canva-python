# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReplyCreateParams"]


class ReplyCreateParams(TypedDict, total=False):
    design_id: Required[Annotated[str, PropertyInfo(alias="designId")]]

    message_plaintext: Required[str]
    """The comment message of the reply in plaintext.

    This is the reply comment shown in the Canva UI.

    You can also mention users in your message by specifying their User ID and Team
    ID using the format `[user_id:team_id]`.
    """
