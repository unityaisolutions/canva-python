# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .replies import (
    RepliesResource,
    AsyncRepliesResource,
    RepliesResourceWithRawResponse,
    AsyncRepliesResourceWithRawResponse,
    RepliesResourceWithStreamingResponse,
    AsyncRepliesResourceWithStreamingResponse,
)
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
from ....types.designs import comment_create_params
from ....types.designs.comment_create_response import CommentCreateResponse
from ....types.designs.comment_retrieve_response import CommentRetrieveResponse

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    @cached_property
    def replies(self) -> RepliesResource:
        return RepliesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    def create(
        self,
        design_id: str,
        *,
        message_plaintext: str,
        assignee_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateResponse:
        """<Warning>
        This API is currently provided as a preview.

        Be aware of the following:
        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
        </Warning>

        Creates a new comment thread on a design. For information on comments and how
        they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          message_plaintext: The comment message in plaintext. This is the comment body shown in the Canva
              UI.

              You can also mention users in your message by specifying their User ID and Team
              ID using the format `[user_id:team_id]`. If the `assignee_id` parameter is
              specified, you must mention the assignee in the message.

          assignee_id: Lets you assign the comment to a Canva user using their User ID. You _must_
              mention the assigned user in the `message`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return self._post(
            f"/v1/designs/{design_id}/comments",
            body=maybe_transform(
                {
                    "message_plaintext": message_plaintext,
                    "assignee_id": assignee_id,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    def retrieve(
        self,
        thread_id: str,
        *,
        design_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Gets a comment or suggestion thread on a design. To retrieve a reply to a
        comment thread, use the
        [Get reply](https://www.canva.dev/docs/connect/api-reference/comments/get-reply/)
        API. For information on comments and how they're used in the Canva UI, see the
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
        return self._get(
            f"/v1/designs/{design_id}/comments/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentRetrieveResponse,
        )


class AsyncCommentsResource(AsyncAPIResource):
    @cached_property
    def replies(self) -> AsyncRepliesResource:
        return AsyncRepliesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    async def create(
        self,
        design_id: str,
        *,
        message_plaintext: str,
        assignee_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateResponse:
        """<Warning>
        This API is currently provided as a preview.

        Be aware of the following:
        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process, and can't be made available to all Canva users.
        </Warning>

        Creates a new comment thread on a design. For information on comments and how
        they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          message_plaintext: The comment message in plaintext. This is the comment body shown in the Canva
              UI.

              You can also mention users in your message by specifying their User ID and Team
              ID using the format `[user_id:team_id]`. If the `assignee_id` parameter is
              specified, you must mention the assignee in the message.

          assignee_id: Lets you assign the comment to a Canva user using their User ID. You _must_
              mention the assigned user in the `message`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return await self._post(
            f"/v1/designs/{design_id}/comments",
            body=await async_maybe_transform(
                {
                    "message_plaintext": message_plaintext,
                    "assignee_id": assignee_id,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    async def retrieve(
        self,
        thread_id: str,
        *,
        design_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Gets a comment or suggestion thread on a design. To retrieve a reply to a
        comment thread, use the
        [Get reply](https://www.canva.dev/docs/connect/api-reference/comments/get-reply/)
        API. For information on comments and how they're used in the Canva UI, see the
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
        return await self._get(
            f"/v1/designs/{design_id}/comments/{thread_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentRetrieveResponse,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_raw_response_wrapper(
            comments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            comments.retrieve,
        )

    @cached_property
    def replies(self) -> RepliesResourceWithRawResponse:
        return RepliesResourceWithRawResponse(self._comments.replies)


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_raw_response_wrapper(
            comments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            comments.retrieve,
        )

    @cached_property
    def replies(self) -> AsyncRepliesResourceWithRawResponse:
        return AsyncRepliesResourceWithRawResponse(self._comments.replies)


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_streamed_response_wrapper(
            comments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            comments.retrieve,
        )

    @cached_property
    def replies(self) -> RepliesResourceWithStreamingResponse:
        return RepliesResourceWithStreamingResponse(self._comments.replies)


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_streamed_response_wrapper(
            comments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            comments.retrieve,
        )

    @cached_property
    def replies(self) -> AsyncRepliesResourceWithStreamingResponse:
        return AsyncRepliesResourceWithStreamingResponse(self._comments.replies)
