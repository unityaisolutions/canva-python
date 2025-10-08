# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import resize_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.resize_create_response import ResizeCreateResponse
from ..types.design_type_input_param import DesignTypeInputParam
from ..types.resize_retrieve_response import ResizeRetrieveResponse

__all__ = ["ResizesResource", "AsyncResizesResource"]


class ResizesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResizesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return ResizesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResizesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return ResizesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design_id: str,
        design_type: DesignTypeInputParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResizeCreateResponse:
        """
        <Note>

        To use this API, your integration must act on behalf of a user that's on a Canva
        plan with premium features (such as Canva Pro).

        </Note>

        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to create a resized copy of a design. The new resized design is added to the top
        level of the user's
        [projects](https://www.canva.com/help/find-designs-and-folders/) (`root`
        folder).

        To resize a design into a new design, you can either:

        - Use a preset design type.
        - Set height and width dimensions for a custom design.

        Note the following behaviors and restrictions when resizing designs:

        - Designs can be resized to a maximum area of 25,000,000 pixels squared.
        - Resizing designs using the Connect API always creates a new design. In-place
          resizing is currently not available in the Connect API, but can be done in the
          Canva UI.
        - Resizing a multi-page design results in all pages of the design being resized.
          Resizing a section of a design is only available in the Canva UI.
        - [Canva docs](https://www.canva.com/create/documents/) can't be resized, and
          other design types can't be resized to a Canva doc.
        - Canva Code designs can't be resized, and other design types can't be resized
          to a Canva Code design.

        <Note>
        For more information on the workflow for using asynchronous jobs,
        see [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of resize jobs created with this API using the
        [Get design resize job API](https://www.canva.dev/docs/connect/api-reference/resizes/get-design-resize-job/).
        </Note>

        Args:
          design_id: The design ID.

          design_type: The desired design type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/resizes",
            body=maybe_transform(
                {
                    "design_id": design_id,
                    "design_type": design_type,
                },
                resize_create_params.ResizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResizeCreateResponse,
        )

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResizeRetrieveResponse:
        """
        <Note>

        To use this API, your integration must act on behalf of a user that's on a Canva
        plan with premium features (such as Canva Pro).

        </Note>

        Gets the result of a design resize job that was created using the
        [Create design resize job API](https://www.canva.dev/docs/connect/api-reference/resizes/create-design-resize-job/).

        If the job is successful, the response includes a summary of the new resized
        design, including its metadata.

        You might need to make multiple requests to this endpoint until you get a
        `success` or `failed` status. For more information on the workflow for using
        asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/resizes/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResizeRetrieveResponse,
        )


class AsyncResizesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResizesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResizesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResizesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncResizesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design_id: str,
        design_type: DesignTypeInputParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResizeCreateResponse:
        """
        <Note>

        To use this API, your integration must act on behalf of a user that's on a Canva
        plan with premium features (such as Canva Pro).

        </Note>

        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to create a resized copy of a design. The new resized design is added to the top
        level of the user's
        [projects](https://www.canva.com/help/find-designs-and-folders/) (`root`
        folder).

        To resize a design into a new design, you can either:

        - Use a preset design type.
        - Set height and width dimensions for a custom design.

        Note the following behaviors and restrictions when resizing designs:

        - Designs can be resized to a maximum area of 25,000,000 pixels squared.
        - Resizing designs using the Connect API always creates a new design. In-place
          resizing is currently not available in the Connect API, but can be done in the
          Canva UI.
        - Resizing a multi-page design results in all pages of the design being resized.
          Resizing a section of a design is only available in the Canva UI.
        - [Canva docs](https://www.canva.com/create/documents/) can't be resized, and
          other design types can't be resized to a Canva doc.
        - Canva Code designs can't be resized, and other design types can't be resized
          to a Canva Code design.

        <Note>
        For more information on the workflow for using asynchronous jobs,
        see [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of resize jobs created with this API using the
        [Get design resize job API](https://www.canva.dev/docs/connect/api-reference/resizes/get-design-resize-job/).
        </Note>

        Args:
          design_id: The design ID.

          design_type: The desired design type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/resizes",
            body=await async_maybe_transform(
                {
                    "design_id": design_id,
                    "design_type": design_type,
                },
                resize_create_params.ResizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResizeCreateResponse,
        )

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResizeRetrieveResponse:
        """
        <Note>

        To use this API, your integration must act on behalf of a user that's on a Canva
        plan with premium features (such as Canva Pro).

        </Note>

        Gets the result of a design resize job that was created using the
        [Create design resize job API](https://www.canva.dev/docs/connect/api-reference/resizes/create-design-resize-job/).

        If the job is successful, the response includes a summary of the new resized
        design, including its metadata.

        You might need to make multiple requests to this endpoint until you get a
        `success` or `failed` status. For more information on the workflow for using
        asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/resizes/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResizeRetrieveResponse,
        )


class ResizesResourceWithRawResponse:
    def __init__(self, resizes: ResizesResource) -> None:
        self._resizes = resizes

        self.create = to_raw_response_wrapper(
            resizes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            resizes.retrieve,
        )


class AsyncResizesResourceWithRawResponse:
    def __init__(self, resizes: AsyncResizesResource) -> None:
        self._resizes = resizes

        self.create = async_to_raw_response_wrapper(
            resizes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            resizes.retrieve,
        )


class ResizesResourceWithStreamingResponse:
    def __init__(self, resizes: ResizesResource) -> None:
        self._resizes = resizes

        self.create = to_streamed_response_wrapper(
            resizes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            resizes.retrieve,
        )


class AsyncResizesResourceWithStreamingResponse:
    def __init__(self, resizes: AsyncResizesResource) -> None:
        self._resizes = resizes

        self.create = async_to_streamed_response_wrapper(
            resizes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            resizes.retrieve,
        )
