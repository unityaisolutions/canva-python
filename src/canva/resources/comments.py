# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions

import httpx

from ..types import comment_create_reply_params, comment_create_thread_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.comment_object_input_param import CommentObjectInputParam
from ..types.comment_create_reply_response import CommentCreateReplyResponse
from ..types.comment_create_thread_response import CommentCreateThreadResponse

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create_reply(
        self,
        comment_id: str,
        *,
        attached_to: CommentObjectInputParam,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateReplyResponse:
        """
        <Warning>

        This API is deprecated, so you should use the
        [Create reply](https://www.canva.dev/docs/connect/api-reference/comments/create-reply/)
        API instead.

        </Warning>

        <Warning>

        This API is currently provided as a preview. Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Creates a reply to a comment in a design. To reply to an existing thread of
        comments, you can use either the `id` of the parent (original) comment, or the
        `thread_id` of a comment in the thread. Each comment can have a maximum of 100
        replies created for it.

        For information on comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          attached_to: If the comment is attached to a Canva Design.

          message: The reply comment message. This is the reply comment body shown in the Canva UI.

              You can also mention users in your message by specifying their User ID and Team
              ID using the format `[user_id:team_id]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return self._post(
            f"/v1/comments/{comment_id}/replies",
            body=maybe_transform(
                {
                    "attached_to": attached_to,
                    "message": message,
                },
                comment_create_reply_params.CommentCreateReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateReplyResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def create_thread(
        self,
        *,
        attached_to: CommentObjectInputParam,
        message: str,
        assignee_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateThreadResponse:
        """
        <Warning>

        This API is deprecated, so you should use the
        [Create thread](https://www.canva.dev/docs/connect/api-reference/comments/create-thread/)
        API instead.

        </Warning>

        <Warning>

        This API is currently provided as a preview. Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Create a new top-level comment on a design. For information on comments and how
        they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/). A design can have a
        maximum of 1000 comments.

        Args:
          attached_to: If the comment is attached to a Canva Design.

          message: The comment message. This is the comment body shown in the Canva UI.

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
        return self._post(
            "/v1/comments",
            body=maybe_transform(
                {
                    "attached_to": attached_to,
                    "message": message,
                    "assignee_id": assignee_id,
                },
                comment_create_thread_params.CommentCreateThreadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateThreadResponse,
        )


class AsyncCommentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create_reply(
        self,
        comment_id: str,
        *,
        attached_to: CommentObjectInputParam,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateReplyResponse:
        """
        <Warning>

        This API is deprecated, so you should use the
        [Create reply](https://www.canva.dev/docs/connect/api-reference/comments/create-reply/)
        API instead.

        </Warning>

        <Warning>

        This API is currently provided as a preview. Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Creates a reply to a comment in a design. To reply to an existing thread of
        comments, you can use either the `id` of the parent (original) comment, or the
        `thread_id` of a comment in the thread. Each comment can have a maximum of 100
        replies created for it.

        For information on comments and how they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/).

        Args:
          attached_to: If the comment is attached to a Canva Design.

          message: The reply comment message. This is the reply comment body shown in the Canva UI.

              You can also mention users in your message by specifying their User ID and Team
              ID using the format `[user_id:team_id]`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        return await self._post(
            f"/v1/comments/{comment_id}/replies",
            body=await async_maybe_transform(
                {
                    "attached_to": attached_to,
                    "message": message,
                },
                comment_create_reply_params.CommentCreateReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateReplyResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def create_thread(
        self,
        *,
        attached_to: CommentObjectInputParam,
        message: str,
        assignee_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateThreadResponse:
        """
        <Warning>

        This API is deprecated, so you should use the
        [Create thread](https://www.canva.dev/docs/connect/api-reference/comments/create-thread/)
        API instead.

        </Warning>

        <Warning>

        This API is currently provided as a preview. Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Create a new top-level comment on a design. For information on comments and how
        they're used in the Canva UI, see the
        [Canva Help Center](https://www.canva.com/help/comments/). A design can have a
        maximum of 1000 comments.

        Args:
          attached_to: If the comment is attached to a Canva Design.

          message: The comment message. This is the comment body shown in the Canva UI.

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
        return await self._post(
            "/v1/comments",
            body=await async_maybe_transform(
                {
                    "attached_to": attached_to,
                    "message": message,
                    "assignee_id": assignee_id,
                },
                comment_create_thread_params.CommentCreateThreadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateThreadResponse,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create_reply = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                comments.create_reply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_thread = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                comments.create_thread,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create_reply = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                comments.create_reply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_thread = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                comments.create_thread,  # pyright: ignore[reportDeprecated],
            )
        )


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create_reply = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                comments.create_reply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_thread = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                comments.create_thread,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create_reply = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                comments.create_reply,  # pyright: ignore[reportDeprecated],
            )
        )
        self.create_thread = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                comments.create_thread,  # pyright: ignore[reportDeprecated],
            )
        )
