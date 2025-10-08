# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import oauth_create_token_params, oauth_revoke_token_params, oauth_introspect_token_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.oauth_create_token_response import OAuthCreateTokenResponse
from ..types.oauth_introspect_token_response import OAuthIntrospectTokenResponse

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)

    @overload
    def create_token(
        self,
        *,
        code: str,
        code_verifier: str,
        grant_type: Literal["authorization_code"],
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateTokenResponse:
        """
        This endpoint implements the OAuth 2.0 `token` endpoint, as part of the
        Authorization Code flow with Proof Key for Code Exchange (PKCE). For more
        information, see
        [Authentication](https://www.canva.dev/docs/connect/authentication/).

        To generate an access token, you must provide one of the following:

        - An authorization code
        - A refresh token

        Generating a token using either an authorization code or a refresh token allows
        your integration to act on behalf of a user. You must first
        [obtain user authorization and get an authorization code](https://www.canva.dev/docs/connect/authentication/#obtain-user-authorization).

        Access tokens may be up to 4 KB in size, and are only valid for a specified
        period of time. The expiry time (currently 4 hours) is shown in the endpoint
        response and is subject to change.

        **Endpoint authentication**

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        **Generate an access token using an authorization code**

        To generate an access token with an authorization code, you must:

        - Set `grant_type` to `authorization_code`.
        - Provide the `code_verifier` value that you generated when creating the user
          authorization URL.
        - Provide the authorization code you received after the user authorized the
          integration.

        **Generate an access token using a refresh token**

        Using the `refresh_token` value from a previous user token request, you can get
        a new access token with the same or smaller scope as the previous one, but with
        a refreshed expiry time. You will also receive a new refresh token that you can
        use to refresh the access token again.

        To refresh an existing access token, you must:

        - Set `grant_type` to `refresh_token`.
        - Provide the `refresh_token` from a previous token request.

        Args:
          code: The authorization code you received after the user authorized the integration.

          code_verifier: The `code_verifier` value that you generated when creating the user
              authorization URL.

          grant_type: For exchanging an authorization code for an access token.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          redirect_uri: Only required if a redirect URL was supplied when you
              [created the user authorization URL](https://www.canva.dev/docs/connect/authentication/#create-the-authorization-url).

              Must be one of those already specified by the client. If not supplied, the first
              redirect_uri defined for the client will be used by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_token(
        self,
        *,
        grant_type: Literal["refresh_token"],
        refresh_token: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateTokenResponse:
        """
        This endpoint implements the OAuth 2.0 `token` endpoint, as part of the
        Authorization Code flow with Proof Key for Code Exchange (PKCE). For more
        information, see
        [Authentication](https://www.canva.dev/docs/connect/authentication/).

        To generate an access token, you must provide one of the following:

        - An authorization code
        - A refresh token

        Generating a token using either an authorization code or a refresh token allows
        your integration to act on behalf of a user. You must first
        [obtain user authorization and get an authorization code](https://www.canva.dev/docs/connect/authentication/#obtain-user-authorization).

        Access tokens may be up to 4 KB in size, and are only valid for a specified
        period of time. The expiry time (currently 4 hours) is shown in the endpoint
        response and is subject to change.

        **Endpoint authentication**

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        **Generate an access token using an authorization code**

        To generate an access token with an authorization code, you must:

        - Set `grant_type` to `authorization_code`.
        - Provide the `code_verifier` value that you generated when creating the user
          authorization URL.
        - Provide the authorization code you received after the user authorized the
          integration.

        **Generate an access token using a refresh token**

        Using the `refresh_token` value from a previous user token request, you can get
        a new access token with the same or smaller scope as the previous one, but with
        a refreshed expiry time. You will also receive a new refresh token that you can
        use to refresh the access token again.

        To refresh an existing access token, you must:

        - Set `grant_type` to `refresh_token`.
        - Provide the `refresh_token` from a previous token request.

        Args:
          grant_type: For generating an access token using a refresh token.

          refresh_token: The refresh token to be exchanged. You can copy this value from the successful
              response received when generating an access token.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          scope: Optional scope value when refreshing an access token. Separate multiple
              [scopes](https://www.canva.dev/docs/connect/appendix/scopes/) with a single
              space between each scope.

              The requested scope cannot include any permissions not already granted, so this
              parameter allows you to limit the scope when refreshing a token. If omitted, the
              scope for the token remains unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["code", "code_verifier", "grant_type"], ["grant_type", "refresh_token"])
    def create_token(
        self,
        *,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        grant_type: Literal["authorization_code"] | Literal["refresh_token"],
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateTokenResponse:
        return self._post(
            "/v1/oauth/token",
            body=maybe_transform(
                {
                    "code": code,
                    "code_verifier": code_verifier,
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                oauth_create_token_params.OAuthCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCreateTokenResponse,
        )

    def introspect_token(
        self,
        *,
        token: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthIntrospectTokenResponse:
        """Introspect an access token to see whether it is valid and active.

        You can also
        verify some token properties, such as its claims, scopes, and validity times.

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        Args:
          token: The token to introspect.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/oauth/introspect",
            body=maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                oauth_introspect_token_params.OAuthIntrospectTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthIntrospectTokenResponse,
        )

    def revoke_token(
        self,
        *,
        token: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Revoke an access token or a refresh token.

        If you revoke a _refresh token_, be aware that:

        - The refresh token's lineage is also revoked. This means that access tokens
          created from that refresh token are also revoked.
        - The user's consent for your integration is also revoked. This means that the
          user must go through the OAuth process again to use your integration.

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        Args:
          token: The token to revoke.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/oauth/revoke",
            body=maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                oauth_revoke_token_params.OAuthRevokeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)

    @overload
    async def create_token(
        self,
        *,
        code: str,
        code_verifier: str,
        grant_type: Literal["authorization_code"],
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateTokenResponse:
        """
        This endpoint implements the OAuth 2.0 `token` endpoint, as part of the
        Authorization Code flow with Proof Key for Code Exchange (PKCE). For more
        information, see
        [Authentication](https://www.canva.dev/docs/connect/authentication/).

        To generate an access token, you must provide one of the following:

        - An authorization code
        - A refresh token

        Generating a token using either an authorization code or a refresh token allows
        your integration to act on behalf of a user. You must first
        [obtain user authorization and get an authorization code](https://www.canva.dev/docs/connect/authentication/#obtain-user-authorization).

        Access tokens may be up to 4 KB in size, and are only valid for a specified
        period of time. The expiry time (currently 4 hours) is shown in the endpoint
        response and is subject to change.

        **Endpoint authentication**

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        **Generate an access token using an authorization code**

        To generate an access token with an authorization code, you must:

        - Set `grant_type` to `authorization_code`.
        - Provide the `code_verifier` value that you generated when creating the user
          authorization URL.
        - Provide the authorization code you received after the user authorized the
          integration.

        **Generate an access token using a refresh token**

        Using the `refresh_token` value from a previous user token request, you can get
        a new access token with the same or smaller scope as the previous one, but with
        a refreshed expiry time. You will also receive a new refresh token that you can
        use to refresh the access token again.

        To refresh an existing access token, you must:

        - Set `grant_type` to `refresh_token`.
        - Provide the `refresh_token` from a previous token request.

        Args:
          code: The authorization code you received after the user authorized the integration.

          code_verifier: The `code_verifier` value that you generated when creating the user
              authorization URL.

          grant_type: For exchanging an authorization code for an access token.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          redirect_uri: Only required if a redirect URL was supplied when you
              [created the user authorization URL](https://www.canva.dev/docs/connect/authentication/#create-the-authorization-url).

              Must be one of those already specified by the client. If not supplied, the first
              redirect_uri defined for the client will be used by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_token(
        self,
        *,
        grant_type: Literal["refresh_token"],
        refresh_token: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateTokenResponse:
        """
        This endpoint implements the OAuth 2.0 `token` endpoint, as part of the
        Authorization Code flow with Proof Key for Code Exchange (PKCE). For more
        information, see
        [Authentication](https://www.canva.dev/docs/connect/authentication/).

        To generate an access token, you must provide one of the following:

        - An authorization code
        - A refresh token

        Generating a token using either an authorization code or a refresh token allows
        your integration to act on behalf of a user. You must first
        [obtain user authorization and get an authorization code](https://www.canva.dev/docs/connect/authentication/#obtain-user-authorization).

        Access tokens may be up to 4 KB in size, and are only valid for a specified
        period of time. The expiry time (currently 4 hours) is shown in the endpoint
        response and is subject to change.

        **Endpoint authentication**

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        **Generate an access token using an authorization code**

        To generate an access token with an authorization code, you must:

        - Set `grant_type` to `authorization_code`.
        - Provide the `code_verifier` value that you generated when creating the user
          authorization URL.
        - Provide the authorization code you received after the user authorized the
          integration.

        **Generate an access token using a refresh token**

        Using the `refresh_token` value from a previous user token request, you can get
        a new access token with the same or smaller scope as the previous one, but with
        a refreshed expiry time. You will also receive a new refresh token that you can
        use to refresh the access token again.

        To refresh an existing access token, you must:

        - Set `grant_type` to `refresh_token`.
        - Provide the `refresh_token` from a previous token request.

        Args:
          grant_type: For generating an access token using a refresh token.

          refresh_token: The refresh token to be exchanged. You can copy this value from the successful
              response received when generating an access token.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          scope: Optional scope value when refreshing an access token. Separate multiple
              [scopes](https://www.canva.dev/docs/connect/appendix/scopes/) with a single
              space between each scope.

              The requested scope cannot include any permissions not already granted, so this
              parameter allows you to limit the scope when refreshing a token. If omitted, the
              scope for the token remains unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["code", "code_verifier", "grant_type"], ["grant_type", "refresh_token"])
    async def create_token(
        self,
        *,
        code: str | Omit = omit,
        code_verifier: str | Omit = omit,
        grant_type: Literal["authorization_code"] | Literal["refresh_token"],
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        redirect_uri: str | Omit = omit,
        refresh_token: str | Omit = omit,
        scope: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthCreateTokenResponse:
        return await self._post(
            "/v1/oauth/token",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "code_verifier": code_verifier,
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,
                    "refresh_token": refresh_token,
                    "scope": scope,
                },
                oauth_create_token_params.OAuthCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthCreateTokenResponse,
        )

    async def introspect_token(
        self,
        *,
        token: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthIntrospectTokenResponse:
        """Introspect an access token to see whether it is valid and active.

        You can also
        verify some token properties, such as its claims, scopes, and validity times.

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        Args:
          token: The token to introspect.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/oauth/introspect",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                oauth_introspect_token_params.OAuthIntrospectTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthIntrospectTokenResponse,
        )

    async def revoke_token(
        self,
        *,
        token: str,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Revoke an access token or a refresh token.

        If you revoke a _refresh token_, be aware that:

        - The refresh token's lineage is also revoked. This means that access tokens
          created from that refresh token are also revoked.
        - The user's consent for your integration is also revoked. This means that the
          user must go through the OAuth process again to use your integration.

        Requests to this endpoint require authentication with your client ID and client
        secret, using _one_ of the following methods:

        - **Basic access authentication** (Recommended): For
          [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication),
          the `{credentials}` string must be a Base64 encoded value of
          `{client id}:{client secret}`.
        - **Body parameters**: Provide your integration's credentials using the
          `client_id` and `client_secret` body parameters.

        This endpoint can't be called from a user's web-browser client because it uses
        client authentication with client secrets. Requests must come from your
        integration's backend, otherwise they'll be blocked by Canva's
        [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
        policy.

        Args:
          token: The token to revoke.

          client_id: Your integration's unique ID, for authenticating the request.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          client_secret: Your integration's client secret, for authenticating the request. Begins with
              `cnvca`.

              NOTE: We recommend that you use basic access authentication instead of
              specifying `client_id` and `client_secret` as body parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/oauth/revoke",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                oauth_revoke_token_params.OAuthRevokeTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.create_token = to_raw_response_wrapper(
            oauth.create_token,
        )
        self.introspect_token = to_raw_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = to_raw_response_wrapper(
            oauth.revoke_token,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.create_token = async_to_raw_response_wrapper(
            oauth.create_token,
        )
        self.introspect_token = async_to_raw_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = async_to_raw_response_wrapper(
            oauth.revoke_token,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.create_token = to_streamed_response_wrapper(
            oauth.create_token,
        )
        self.introspect_token = to_streamed_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = to_streamed_response_wrapper(
            oauth.revoke_token,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.create_token = async_to_streamed_response_wrapper(
            oauth.create_token,
        )
        self.introspect_token = async_to_streamed_response_wrapper(
            oauth.introspect_token,
        )
        self.revoke_token = async_to_streamed_response_wrapper(
            oauth.revoke_token,
        )
