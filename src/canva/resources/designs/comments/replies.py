# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.designs.comments import reply_list_params, reply_create_params
from ....types.designs.comments.reply_list_response import ReplyListResponse
from ....types.designs.comments.reply_create_response import ReplyCreateResponse
from ....types.designs.comments.reply_retrieve_response import ReplyRetrieveResponse

__all__ = ["RepliesResource", "AsyncRepliesResource"]


class RepliesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RepliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return RepliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RepliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return RepliesResourceWithStreamingResponse(self)

    def create(
        self,
        thread_id: str,
        *,
        design_id: str,
        message_plaintext: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplyCreateResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Creates a reply to a comment or suggestion thread on a design. To reply to an
        existing thread, you must provide the ID of the thread which is returned when a
        thread is created, or from the `thread_id` value of an existing reply in the
        thread. Each thread can have a maximum of 100 replies created for it.

        For information on comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          message_plaintext: The comment message of the reply in plaintext. This is the reply comment shown
              in the Canva UI.

              You can also mention users in your message by specifying their User ID and Team
              ID using the format `[user_id:team_id]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._post(
            f"/v1/designs/{design_id}/comments/{thread_id}/replies",
            body=maybe_transform({"message_plaintext": message_plaintext}, reply_create_params.ReplyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyCreateResponse,
        )

    def retrieve(
        self,
        reply_id: str,
        *,
        design_id: str,
        thread_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplyRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Gets a reply to a comment or suggestion thread on a design. For information on
        comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        if not reply_id:
            raise ValueError(f"Expected a non-empty value for `reply_id` but received {reply_id!r}")
        return self._get(
            f"/v1/designs/{design_id}/comments/{thread_id}/replies/{reply_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyRetrieveResponse,
        )

    def list(
        self,
        thread_id: str,
        *,
        design_id: str,
        continuation: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplyListResponse:
        """<Warning>
        This API is currently provided as a preview.

        Be aware of the following:
        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
        </Warning>

        Retrieves a list of replies for a comment or suggestion thread on a design.

        For information on comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          continuation: If the success response contains a continuation token, the list contains more
              items you can list. You can use this token as a query parameter and retrieve
              more items from the list, for example `?continuation={continuation}`.

              To retrieve all items, you might need to make multiple requests.

          limit: The number of replies to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return self._get(
            f"/v1/designs/{design_id}/comments/{thread_id}/replies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuation": continuation,
                        "limit": limit,
                    },
                    reply_list_params.ReplyListParams,
                ),
            ),
            cast_to=ReplyListResponse,
        )


class AsyncRepliesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRepliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRepliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRepliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncRepliesResourceWithStreamingResponse(self)

    async def create(
        self,
        thread_id: str,
        *,
        design_id: str,
        message_plaintext: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplyCreateResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Creates a reply to a comment or suggestion thread on a design. To reply to an
        existing thread, you must provide the ID of the thread which is returned when a
        thread is created, or from the `thread_id` value of an existing reply in the
        thread. Each thread can have a maximum of 100 replies created for it.

        For information on comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          message_plaintext: The comment message of the reply in plaintext. This is the reply comment shown
              in the Canva UI.

              You can also mention users in your message by specifying their User ID and Team
              ID using the format `[user_id:team_id]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._post(
            f"/v1/designs/{design_id}/comments/{thread_id}/replies",
            body=await async_maybe_transform(
                {"message_plaintext": message_plaintext}, reply_create_params.ReplyCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyCreateResponse,
        )

    async def retrieve(
        self,
        reply_id: str,
        *,
        design_id: str,
        thread_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplyRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Gets a reply to a comment or suggestion thread on a design. For information on
        comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        if not reply_id:
            raise ValueError(f"Expected a non-empty value for `reply_id` but received {reply_id!r}")
        return await self._get(
            f"/v1/designs/{design_id}/comments/{thread_id}/replies/{reply_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReplyRetrieveResponse,
        )

    async def list(
        self,
        thread_id: str,
        *,
        design_id: str,
        continuation: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReplyListResponse:
        """<Warning>
        This API is currently provided as a preview.

        Be aware of the following:
        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
        </Warning>

        Retrieves a list of replies for a comment or suggestion thread on a design.

        For information on comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          continuation: If the success response contains a continuation token, the list contains more
              items you can list. You can use this token as a query parameter and retrieve
              more items from the list, for example `?continuation={continuation}`.

              To retrieve all items, you might need to make multiple requests.

          limit: The number of replies to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        if not thread_id:
            raise ValueError(f"Expected a non-empty value for `thread_id` but received {thread_id!r}")
        return await self._get(
            f"/v1/designs/{design_id}/comments/{thread_id}/replies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continuation": continuation,
                        "limit": limit,
                    },
                    reply_list_params.ReplyListParams,
                ),
            ),
            cast_to=ReplyListResponse,
        )


class RepliesResourceWithRawResponse:
    def __init__(self, replies: RepliesResource) -> None:
        self._replies = replies

        self.create = to_raw_response_wrapper(
            replies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            replies.retrieve,
        )
        self.list = to_raw_response_wrapper(
            replies.list,
        )


class AsyncRepliesResourceWithRawResponse:
    def __init__(self, replies: AsyncRepliesResource) -> None:
        self._replies = replies

        self.create = async_to_raw_response_wrapper(
            replies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            replies.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            replies.list,
        )


class RepliesResourceWithStreamingResponse:
    def __init__(self, replies: RepliesResource) -> None:
        self._replies = replies

        self.create = to_streamed_response_wrapper(
            replies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            replies.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            replies.list,
        )


class AsyncRepliesResourceWithStreamingResponse:
    def __init__(self, replies: AsyncRepliesResource) -> None:
        self._replies = replies

        self.create = async_to_streamed_response_wrapper(
            replies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            replies.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            replies.list,
        )
