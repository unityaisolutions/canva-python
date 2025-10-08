# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import export_create_params
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
from ..types.export_create_response import ExportCreateResponse
from ..types.export_retrieve_response import ExportRetrieveResponse

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design_id: str,
        format: export_create_params.Format,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to export a file from Canva. Once the exported file is generated, you can
        download it using the URL(s) provided. The download URLs are only valid for 24
        hours.

        The request requires the design ID and the exported file format type.

        Supported file formats (and export file type values): PDF (`pdf`), JPG (`jpg`),
        PNG (`png`), GIF (`gif`), Microsoft PowerPoint (`pptx`), and MP4 (`mp4`).

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of export jobs created with this
        API using the
        [Get design export job API](https://www.canva.dev/docs/connect/api-reference/exports/get-design-export-job/).

        </Note>

        Args:
          design_id: The design ID.

          format: Details about the desired export format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/exports",
            body=maybe_transform(
                {
                    "design_id": design_id,
                    "format": format,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportCreateResponse,
        )

    def retrieve(
        self,
        export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportRetrieveResponse:
        """
        Gets the result of a design export job that was created using the
        [Create design export job API](https://www.canva.dev/docs/connect/api-reference/exports/create-design-export-job/).

        If the job is successful, the response includes an array of download URLs.
        Depending on the design type and export format, there is a download URL for each
        page in the design. The download URLs are only valid for 24 hours.

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
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return self._get(
            f"/v1/exports/{export_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportRetrieveResponse,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design_id: str,
        format: export_create_params.Format,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to export a file from Canva. Once the exported file is generated, you can
        download it using the URL(s) provided. The download URLs are only valid for 24
        hours.

        The request requires the design ID and the exported file format type.

        Supported file formats (and export file type values): PDF (`pdf`), JPG (`jpg`),
        PNG (`png`), GIF (`gif`), Microsoft PowerPoint (`pptx`), and MP4 (`mp4`).

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of export jobs created with this
        API using the
        [Get design export job API](https://www.canva.dev/docs/connect/api-reference/exports/get-design-export-job/).

        </Note>

        Args:
          design_id: The design ID.

          format: Details about the desired export format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/exports",
            body=await async_maybe_transform(
                {
                    "design_id": design_id,
                    "format": format,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportCreateResponse,
        )

    async def retrieve(
        self,
        export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportRetrieveResponse:
        """
        Gets the result of a design export job that was created using the
        [Create design export job API](https://www.canva.dev/docs/connect/api-reference/exports/create-design-export-job/).

        If the job is successful, the response includes an array of download URLs.
        Depending on the design type and export format, there is a download URL for each
        page in the design. The download URLs are only valid for 24 hours.

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
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return await self._get(
            f"/v1/exports/{export_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportRetrieveResponse,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exports.retrieve,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exports.retrieve,
        )
