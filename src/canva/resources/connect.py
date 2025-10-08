# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.connect_retrieve_keys_response import ConnectRetrieveKeysResponse

__all__ = ["ConnectResource", "AsyncConnectResource"]


class ConnectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return ConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return ConnectResourceWithStreamingResponse(self)

    def retrieve_keys(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectRetrieveKeysResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        The Keys API (`connect/keys`) is a security measure you can use to verify the
        authenticity of webhooks you receive from Canva Connect. The Keys API returns a
        [JSON Web Key (JWK)](https://www.rfc-editor.org/rfc/rfc7517#section-2), which
        you can use to decrypt the webhook signature and verify it came from Canva and
        not a potentially malicious actor. This helps to protect your systems from
        [Replay attacks](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/).

        The keys returned by the Keys API can rotate. We recommend you cache the keys
        you receive from this API where possible, and only access this API when you
        receive a webhook signed with an unrecognized key. This allows you to verify
        webhooks quicker than accessing this API every time you receive a webhook.
        """
        return self._get(
            "/v1/connect/keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectRetrieveKeysResponse,
        )


class AsyncConnectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncConnectResourceWithStreamingResponse(self)

    async def retrieve_keys(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectRetrieveKeysResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        The Keys API (`connect/keys`) is a security measure you can use to verify the
        authenticity of webhooks you receive from Canva Connect. The Keys API returns a
        [JSON Web Key (JWK)](https://www.rfc-editor.org/rfc/rfc7517#section-2), which
        you can use to decrypt the webhook signature and verify it came from Canva and
        not a potentially malicious actor. This helps to protect your systems from
        [Replay attacks](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/).

        The keys returned by the Keys API can rotate. We recommend you cache the keys
        you receive from this API where possible, and only access this API when you
        receive a webhook signed with an unrecognized key. This allows you to verify
        webhooks quicker than accessing this API every time you receive a webhook.
        """
        return await self._get(
            "/v1/connect/keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectRetrieveKeysResponse,
        )


class ConnectResourceWithRawResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.retrieve_keys = to_raw_response_wrapper(
            connect.retrieve_keys,
        )


class AsyncConnectResourceWithRawResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.retrieve_keys = async_to_raw_response_wrapper(
            connect.retrieve_keys,
        )


class ConnectResourceWithStreamingResponse:
    def __init__(self, connect: ConnectResource) -> None:
        self._connect = connect

        self.retrieve_keys = to_streamed_response_wrapper(
            connect.retrieve_keys,
        )


class AsyncConnectResourceWithStreamingResponse:
    def __init__(self, connect: AsyncConnectResource) -> None:
        self._connect = connect

        self.retrieve_keys = async_to_streamed_response_wrapper(
            connect.retrieve_keys,
        )
