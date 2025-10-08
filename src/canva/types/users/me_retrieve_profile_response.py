# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MeRetrieveProfileResponse", "Profile"]


class Profile(BaseModel):
    display_name: Optional[str] = None
    """The name of the user as shown in the Canva UI."""


class MeRetrieveProfileResponse(BaseModel):
    profile: Profile
    """Profile for the user, consisting of the display name and other attributes."""
