# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["OAuthCreateTokenParams", "ExchangeAuthCodeRequest", "ExchangeRefreshTokenRequest"]


class ExchangeAuthCodeRequest(TypedDict, total=False):
    code: Required[str]
    """The authorization code you received after the user authorized the integration."""

    code_verifier: Required[str]
    """
    The `code_verifier` value that you generated when creating the user
    authorization URL.
    """

    grant_type: Required[Literal["authorization_code"]]
    """For exchanging an authorization code for an access token."""

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

    redirect_uri: str
    """
    Only required if a redirect URL was supplied when you
    [created the user authorization URL](https://www.canva.dev/docs/connect/authentication/#create-the-authorization-url).

    Must be one of those already specified by the client. If not supplied, the first
    redirect_uri defined for the client will be used by default.
    """


class ExchangeRefreshTokenRequest(TypedDict, total=False):
    grant_type: Required[Literal["refresh_token"]]
    """For generating an access token using a refresh token."""

    refresh_token: Required[str]
    """The refresh token to be exchanged.

    You can copy this value from the successful response received when generating an
    access token.
    """

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

    scope: str
    """Optional scope value when refreshing an access token.

    Separate multiple [scopes](https://www.canva.dev/docs/connect/appendix/scopes/)
    with a single space between each scope.

    The requested scope cannot include any permissions not already granted, so this
    parameter allows you to limit the scope when refreshing a token. If omitted, the
    scope for the token remains unchanged.
    """


OAuthCreateTokenParams: TypeAlias = Union[ExchangeAuthCodeRequest, ExchangeRefreshTokenRequest]
