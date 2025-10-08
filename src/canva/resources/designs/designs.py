# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .pages import (
    PagesResource,
    AsyncPagesResource,
    PagesResourceWithRawResponse,
    AsyncPagesResourceWithRawResponse,
    PagesResourceWithStreamingResponse,
    AsyncPagesResourceWithStreamingResponse,
)
from ...types import SortByType, OwnershipType, design_list_params, design_create_params
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
from .export_formats import (
    ExportFormatsResource,
    AsyncExportFormatsResource,
    ExportFormatsResourceWithRawResponse,
    AsyncExportFormatsResourceWithRawResponse,
    ExportFormatsResourceWithStreamingResponse,
    AsyncExportFormatsResourceWithStreamingResponse,
)
from .comments.comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ...types.sort_by_type import SortByType
from ...types.ownership_type import OwnershipType
from ...types.design_list_response import DesignListResponse
from ...types.design_create_response import DesignCreateResponse
from ...types.design_type_input_param import DesignTypeInputParam
from ...types.design_retrieve_response import DesignRetrieveResponse

__all__ = ["DesignsResource", "AsyncDesignsResource"]


class DesignsResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def pages(self) -> PagesResource:
        return PagesResource(self._client)

    @cached_property
    def export_formats(self) -> ExportFormatsResource:
        return ExportFormatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DesignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return DesignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DesignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return DesignsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        asset_id: str | Omit = omit,
        design_type: DesignTypeInputParam | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignCreateResponse:
        """Creates a new Canva design.

        To create a new design, you can either:

        - Use a preset design type.
        - Set height and width dimensions for a custom design.

        Additionally, you can also provide the `asset_id` of an asset in the user's
        [projects](https://www.canva.com/help/find-designs-and-folders/) to add to the
        new design. Currently, this only supports image assets. To list the assets in a
        folder in the user's projects, use the
        [List folder items API](https://www.canva.dev/docs/connect/api-reference/folders/list-folder-items/).

        NOTE: Blank designs created with this API are automatically deleted if they're
        not edited within 7 days. These blank designs bypass the user's Canva trash and
        are permanently deleted.

        Args:
          asset_id: The ID of an asset to insert into the created design. Currently, this only
              supports image assets.

          design_type: The desired design type.

          title: The name of the design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/designs",
            body=maybe_transform(
                {
                    "asset_id": asset_id,
                    "design_type": design_type,
                    "title": title,
                },
                design_create_params.DesignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignCreateResponse,
        )

    def retrieve(
        self,
        design_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignRetrieveResponse:
        """Gets the metadata for a design.

        This includes owner information, URLs for
        editing and viewing, and thumbnail information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return self._get(
            f"/v1/designs/{design_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignRetrieveResponse,
        )

    def list(
        self,
        *,
        continuation: str | Omit = omit,
        ownership: OwnershipType | Omit = omit,
        query: str | Omit = omit,
        sort_by: SortByType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignListResponse:
        """
        Lists metadata for all the designs in a Canva user's
        [projects](https://www.canva.com/help/find-designs-and-folders/). You can also:

        - Use search terms to filter the listed designs.
        - Show designs either created by, or shared with the user.
        - Sort the results.

        Args:
          continuation: If the success response contains a continuation token, the list contains more
              designs you can list. You can use this token as a query parameter and retrieve
              more designs from the list, for example
              `/v1/designs?continuation={continuation}`.

              To retrieve all of a user's designs, you might need to make multiple requests.

          ownership: Filter the list of designs based on the user's ownership of the designs.

          query: Lets you search the user's designs, and designs shared with the user, using a
              search term or terms.

          sort_by: Sort the list of designs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/designs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuation": continuation,
                        "ownership": ownership,
                        "query": query,
                        "sort_by": sort_by,
                    },
                    design_list_params.DesignListParams,
                ),
            ),
            cast_to=DesignListResponse,
        )


class AsyncDesignsResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def pages(self) -> AsyncPagesResource:
        return AsyncPagesResource(self._client)

    @cached_property
    def export_formats(self) -> AsyncExportFormatsResource:
        return AsyncExportFormatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDesignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDesignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDesignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncDesignsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        asset_id: str | Omit = omit,
        design_type: DesignTypeInputParam | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignCreateResponse:
        """Creates a new Canva design.

        To create a new design, you can either:

        - Use a preset design type.
        - Set height and width dimensions for a custom design.

        Additionally, you can also provide the `asset_id` of an asset in the user's
        [projects](https://www.canva.com/help/find-designs-and-folders/) to add to the
        new design. Currently, this only supports image assets. To list the assets in a
        folder in the user's projects, use the
        [List folder items API](https://www.canva.dev/docs/connect/api-reference/folders/list-folder-items/).

        NOTE: Blank designs created with this API are automatically deleted if they're
        not edited within 7 days. These blank designs bypass the user's Canva trash and
        are permanently deleted.

        Args:
          asset_id: The ID of an asset to insert into the created design. Currently, this only
              supports image assets.

          design_type: The desired design type.

          title: The name of the design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/designs",
            body=await async_maybe_transform(
                {
                    "asset_id": asset_id,
                    "design_type": design_type,
                    "title": title,
                },
                design_create_params.DesignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignCreateResponse,
        )

    async def retrieve(
        self,
        design_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignRetrieveResponse:
        """Gets the metadata for a design.

        This includes owner information, URLs for
        editing and viewing, and thumbnail information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return await self._get(
            f"/v1/designs/{design_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DesignRetrieveResponse,
        )

    async def list(
        self,
        *,
        continuation: str | Omit = omit,
        ownership: OwnershipType | Omit = omit,
        query: str | Omit = omit,
        sort_by: SortByType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DesignListResponse:
        """
        Lists metadata for all the designs in a Canva user's
        [projects](https://www.canva.com/help/find-designs-and-folders/). You can also:

        - Use search terms to filter the listed designs.
        - Show designs either created by, or shared with the user.
        - Sort the results.

        Args:
          continuation: If the success response contains a continuation token, the list contains more
              designs you can list. You can use this token as a query parameter and retrieve
              more designs from the list, for example
              `/v1/designs?continuation={continuation}`.

              To retrieve all of a user's designs, you might need to make multiple requests.

          ownership: Filter the list of designs based on the user's ownership of the designs.

          query: Lets you search the user's designs, and designs shared with the user, using a
              search term or terms.

          sort_by: Sort the list of designs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/designs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continuation": continuation,
                        "ownership": ownership,
                        "query": query,
                        "sort_by": sort_by,
                    },
                    design_list_params.DesignListParams,
                ),
            ),
            cast_to=DesignListResponse,
        )


class DesignsResourceWithRawResponse:
    def __init__(self, designs: DesignsResource) -> None:
        self._designs = designs

        self.create = to_raw_response_wrapper(
            designs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            designs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            designs.list,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._designs.comments)

    @cached_property
    def pages(self) -> PagesResourceWithRawResponse:
        return PagesResourceWithRawResponse(self._designs.pages)

    @cached_property
    def export_formats(self) -> ExportFormatsResourceWithRawResponse:
        return ExportFormatsResourceWithRawResponse(self._designs.export_formats)


class AsyncDesignsResourceWithRawResponse:
    def __init__(self, designs: AsyncDesignsResource) -> None:
        self._designs = designs

        self.create = async_to_raw_response_wrapper(
            designs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            designs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            designs.list,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._designs.comments)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithRawResponse:
        return AsyncPagesResourceWithRawResponse(self._designs.pages)

    @cached_property
    def export_formats(self) -> AsyncExportFormatsResourceWithRawResponse:
        return AsyncExportFormatsResourceWithRawResponse(self._designs.export_formats)


class DesignsResourceWithStreamingResponse:
    def __init__(self, designs: DesignsResource) -> None:
        self._designs = designs

        self.create = to_streamed_response_wrapper(
            designs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            designs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            designs.list,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._designs.comments)

    @cached_property
    def pages(self) -> PagesResourceWithStreamingResponse:
        return PagesResourceWithStreamingResponse(self._designs.pages)

    @cached_property
    def export_formats(self) -> ExportFormatsResourceWithStreamingResponse:
        return ExportFormatsResourceWithStreamingResponse(self._designs.export_formats)


class AsyncDesignsResourceWithStreamingResponse:
    def __init__(self, designs: AsyncDesignsResource) -> None:
        self._designs = designs

        self.create = async_to_streamed_response_wrapper(
            designs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            designs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            designs.list,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._designs.comments)

    @cached_property
    def pages(self) -> AsyncPagesResourceWithStreamingResponse:
        return AsyncPagesResourceWithStreamingResponse(self._designs.pages)

    @cached_property
    def export_formats(self) -> AsyncExportFormatsResourceWithStreamingResponse:
        return AsyncExportFormatsResourceWithStreamingResponse(self._designs.export_formats)
