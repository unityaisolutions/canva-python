# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..user import User
from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..shared.team_user import TeamUser
from .comments.comment_content import CommentContent

__all__ = [
    "Thread",
    "ThreadType",
    "ThreadTypeCommentThreadType",
    "ThreadTypeCommentThreadTypeMentions",
    "ThreadTypeSuggestionThreadType",
    "ThreadTypeSuggestionThreadTypeSuggestedEdit",
    "ThreadTypeSuggestionThreadTypeSuggestedEditAddSuggestedEdit",
    "ThreadTypeSuggestionThreadTypeSuggestedEditDeleteSuggestedEdit",
    "ThreadTypeSuggestionThreadTypeSuggestedEditFormatSuggestedEdit",
]


class ThreadTypeCommentThreadTypeMentions(BaseModel):
    tag: str
    """The mention tag for the user mentioned in the comment thread or reply content.

    This has the format of the user's user ID and team ID separated by a colon
    (`user_id:team_id`).
    """

    user: TeamUser
    """Metadata for the user, consisting of the User ID, Team ID, and display name."""


class ThreadTypeCommentThreadType(BaseModel):
    content: CommentContent
    """The content of a comment thread or reply."""

    mentions: Dict[str, ThreadTypeCommentThreadTypeMentions]
    """The Canva users mentioned in the comment thread or reply."""

    type: Literal["comment"]

    assignee: Optional[User] = None
    """Metadata for the user, consisting of the User ID and display name."""

    resolver: Optional[User] = None
    """Metadata for the user, consisting of the User ID and display name."""


class ThreadTypeSuggestionThreadTypeSuggestedEditAddSuggestedEdit(BaseModel):
    text: str

    type: Literal["add"]


class ThreadTypeSuggestionThreadTypeSuggestedEditDeleteSuggestedEdit(BaseModel):
    text: str

    type: Literal["delete"]


class ThreadTypeSuggestionThreadTypeSuggestedEditFormatSuggestedEdit(BaseModel):
    format: Literal[
        "font_family",
        "font_size",
        "font_weight",
        "font_style",
        "color",
        "background_color",
        "decoration",
        "strikethrough",
        "link",
        "letter_spacing",
        "line_height",
        "direction",
        "text_align",
        "list_marker",
        "list_level",
        "margin_inline_start",
        "text_indent",
        "font_size_modifier",
        "vertical_align",
    ]
    """The suggested format change."""

    type: Literal["format"]


ThreadTypeSuggestionThreadTypeSuggestedEdit: TypeAlias = Annotated[
    Union[
        ThreadTypeSuggestionThreadTypeSuggestedEditAddSuggestedEdit,
        ThreadTypeSuggestionThreadTypeSuggestedEditDeleteSuggestedEdit,
        ThreadTypeSuggestionThreadTypeSuggestedEditFormatSuggestedEdit,
    ],
    PropertyInfo(discriminator="type"),
]


class ThreadTypeSuggestionThreadType(BaseModel):
    status: Literal["open", "accepted", "rejected"]
    """The current status of the suggestion.

    - `open` - A suggestion was made, but it hasn't been accepted or rejected yet.
    - `accepted` - A suggestion was accepted and applied to the design.
    - `rejected` - A suggestion was rejected and not applied to the design.
    """

    suggested_edits: List[ThreadTypeSuggestionThreadTypeSuggestedEdit]

    type: Literal["suggestion"]


ThreadType: TypeAlias = Annotated[
    Union[ThreadTypeCommentThreadType, ThreadTypeSuggestionThreadType], PropertyInfo(discriminator="type")
]


class Thread(BaseModel):
    id: str
    """The ID of the thread.

    You can use this ID to create replies to the thread using the
    [Create reply API](https://www.canva.dev/docs/connect/api-reference/comments/create-reply/).
    """

    created_at: int
    """
    When the thread was created, as a Unix timestamp (in seconds since the Unix
    Epoch).
    """

    design_id: str
    """The ID of the design that the discussion thread is on."""

    thread_type: ThreadType
    """
    The type of the discussion thread, along with additional type-specific
    properties.
    """

    updated_at: int
    """
    When the thread was last updated, as a Unix timestamp (in seconds since the Unix
    Epoch).
    """

    author: Optional[User] = None
    """Metadata for the user, consisting of the User ID and display name."""
