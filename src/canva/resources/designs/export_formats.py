# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.designs.export_format_retrieve_response import ExportFormatRetrieveResponse

__all__ = ["ExportFormatsResource", "AsyncExportFormatsResource"]


class ExportFormatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportFormatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return ExportFormatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportFormatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return ExportFormatsResourceWithStreamingResponse(self)

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
    ) -> ExportFormatRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Lists the available file formats for
        [exporting a design](https://www.canva.dev/docs/connect/api-reference/exports/create-design-export-job/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return self._get(
            f"/v1/designs/{design_id}/export-formats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportFormatRetrieveResponse,
        )


class AsyncExportFormatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportFormatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportFormatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportFormatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncExportFormatsResourceWithStreamingResponse(self)

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
    ) -> ExportFormatRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Lists the available file formats for
        [exporting a design](https://www.canva.dev/docs/connect/api-reference/exports/create-design-export-job/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not design_id:
            raise ValueError(f"Expected a non-empty value for `design_id` but received {design_id!r}")
        return await self._get(
            f"/v1/designs/{design_id}/export-formats",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportFormatRetrieveResponse,
        )


class ExportFormatsResourceWithRawResponse:
    def __init__(self, export_formats: ExportFormatsResource) -> None:
        self._export_formats = export_formats

        self.retrieve = to_raw_response_wrapper(
            export_formats.retrieve,
        )


class AsyncExportFormatsResourceWithRawResponse:
    def __init__(self, export_formats: AsyncExportFormatsResource) -> None:
        self._export_formats = export_formats

        self.retrieve = async_to_raw_response_wrapper(
            export_formats.retrieve,
        )


class ExportFormatsResourceWithStreamingResponse:
    def __init__(self, export_formats: ExportFormatsResource) -> None:
        self._export_formats = export_formats

        self.retrieve = to_streamed_response_wrapper(
            export_formats.retrieve,
        )


class AsyncExportFormatsResourceWithStreamingResponse:
    def __init__(self, export_formats: AsyncExportFormatsResource) -> None:
        self._export_formats = export_formats

        self.retrieve = async_to_streamed_response_wrapper(
            export_formats.retrieve,
        )
