# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TeamUser"]


class TeamUser(BaseModel):
    display_name: Optional[str] = None
    """The name of the user as shown in the Canva UI."""

    team_id: Optional[str] = None
    """The ID of the user's Canva Team."""

    user_id: Optional[str] = None
    """The ID of the user."""
