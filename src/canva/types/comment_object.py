# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CommentObject"]


class CommentObject(BaseModel):
    design_id: str
    """The ID of the design this comment is attached to."""

    type: Literal["design"]
