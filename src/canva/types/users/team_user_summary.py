# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["TeamUserSummary"]


class TeamUserSummary(BaseModel):
    team_id: str
    """The ID of the user's Canva Team."""

    user_id: str
    """The ID of the user."""
