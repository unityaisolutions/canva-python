# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OAuthIntrospectTokenParams"]


class OAuthIntrospectTokenParams(TypedDict, total=False):
    token: Required[str]
    """The token to introspect."""

    client_id: str
    """Your integration's unique ID, for authenticating the request.

    NOTE: We recommend that you use basic access authentication instead of
    specifying `client_id` and `client_secret` as body parameters.
    """

    client_secret: str
    """Your integration's client secret, for authenticating the request.

    Begins with `cnvca`.

    NOTE: We recommend that you use basic access authentication instead of
    specifying `client_id` and `client_secret` as body parameters.
    """
