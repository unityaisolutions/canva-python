# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .team_user_summary import TeamUserSummary

__all__ = ["MeRetrieveResponse"]


class MeRetrieveResponse(BaseModel):
    team_user: TeamUserSummary
    """Metadata for the user, consisting of the User ID and Team ID."""
