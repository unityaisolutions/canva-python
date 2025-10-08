# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str
    """The ID of the user."""

    display_name: Optional[str] = None
    """The name of the user as shown in the Canva UI."""
