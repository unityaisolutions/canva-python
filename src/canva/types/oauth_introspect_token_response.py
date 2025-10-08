# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OAuthIntrospectTokenResponse"]


class OAuthIntrospectTokenResponse(BaseModel):
    active: bool
    """Whether the access token is active.

    If `true`, the access token is valid and active. If `false`, the access token is
    invalid.
    """

    client: Optional[str] = None
    """The ID of the client that requested the token."""

    exp: Optional[int] = None
    """
    The expiration time of the token, as a
    [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) in seconds.
    """

    iat: Optional[int] = None
    """
    When the token was issued, as a
    [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) in seconds.
    """

    jti: Optional[str] = None
    """A unique ID for the access token."""

    nbf: Optional[int] = None
    """
    The "not before" time of the token, which specifies the time before which the
    access token most not be accepted, as a
    [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time) in seconds.
    """

    scope: Optional[str] = None
    """
    The [scopes](https://www.canva.dev/docs/connect/appendix/scopes/) that the token
    has been granted.
    """

    sub: Optional[str] = None
    """The subject of the claim.

    This is the ID of the Canva user that the access token acts on behalf of.

    This is an obfuscated value, so a single user has a unique ID for each
    integration. If the same user authorizes another integration, their ID in that
    other integration is different.
    """
