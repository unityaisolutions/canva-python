# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OAuthCreateTokenResponse"]


class OAuthCreateTokenResponse(BaseModel):
    access_token: str
    """The bearer access token to use to authenticate to Canva Connect API endpoints.

    If requested using a `authorization_code` or `refresh_token`, this allows you to
    act on behalf of a user.
    """

    expires_in: int
    """The expiry time (in seconds) for the token."""

    refresh_token: str
    """The token that you can use to refresh the access token."""

    token_type: str
    """The token type returned. This is always `Bearer`."""

    scope: Optional[str] = None
    """
    The [scopes](https://www.canva.dev/docs/connect/appendix/scopes/) that the token
    has been granted.
    """
