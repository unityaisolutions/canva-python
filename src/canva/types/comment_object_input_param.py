# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommentObjectInputParam"]


class CommentObjectInputParam(TypedDict, total=False):
    design_id: Required[str]
    """The ID of the design you want to attach this comment to."""

    type: Required[Literal["design"]]
