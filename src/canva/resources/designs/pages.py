# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.designs import page_retrieve_params
from ...types.designs.page_retrieve_response import PageRetrieveResponse

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        design_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Lists metadata for pages in a design, such as page-specific thumbnails.

        For the specified design, you can provide `offset` and `limit` values to specify
        the range of pages to return.

        NOTE: Some design types don't have pages (for example, Canva docs).

        Args:
          limit: The number of pages to return, starting at the page index specified using the
              `offset` parameter.

          offset: The page index to start the range of pages to return.

              Pages are indexed using one-based numbering, so the first page in a design has
              the index value `1`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return self._get(
            f"/v1/designs/{design_id}/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    page_retrieve_params.PageRetrieveParams,
                ),
            ),
            cast_to=PageRetrieveResponse,
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        design_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PageRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Lists metadata for pages in a design, such as page-specific thumbnails.

        For the specified design, you can provide `offset` and `limit` values to specify
        the range of pages to return.

        NOTE: Some design types don't have pages (for example, Canva docs).

        Args:
          limit: The number of pages to return, starting at the page index specified using the
              `offset` parameter.

          offset: The page index to start the range of pages to return.

              Pages are indexed using one-based numbering, so the first page in a design has
              the index value `1`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return await self._get(
            f"/v1/designs/{design_id}/pages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    page_retrieve_params.PageRetrieveParams,
                ),
            ),
            cast_to=PageRetrieveResponse,
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.retrieve = to_raw_response_wrapper(
            pages.retrieve,
        )


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.retrieve = async_to_raw_response_wrapper(
            pages.retrieve,
        )


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.retrieve = to_streamed_response_wrapper(
            pages.retrieve,
        )


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.retrieve = async_to_streamed_response_wrapper(
            pages.retrieve,
        )
