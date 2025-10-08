# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._files import read_file_content, async_read_file_content
from .._types import Body, Query, Headers, NotGiven, FileContent, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.import_create_response import ImportCreateResponse
from ..types.import_retrieve_response import ImportRetrieveResponse

__all__ = ["ImportsResource", "AsyncImportsResource"]


class ImportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return ImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return ImportsResourceWithStreamingResponse(self)

    def create(
        self,
        body: FileContent,
        *,
        import_metadata: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to import an external file as a new design in Canva.

        The request format for this endpoint has an `application/octet-stream` body of
        bytes, and the information about the import is provided using an
        `Import-Metadata` header.

        Supported file types for imports are listed in
        [Design imports overview](https://www.canva.dev/docs/connect/api-reference/design-imports/#supported-file-types).

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of design import jobs created with
        this API using the
        [Get design import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/get-design-import-job/).

        </Note>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Import-Metadata": str(import_metadata), **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return self._post(
            "/v1/imports",
            body=read_file_content(body),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportCreateResponse,
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
    ) -> ImportRetrieveResponse:
        """
        Gets the result of a design import job created using the
        [Create design import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/create-design-import-job/).

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
            f"/v1/imports/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportRetrieveResponse,
        )


class AsyncImportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncImportsResourceWithStreamingResponse(self)

    async def create(
        self,
        body: FileContent,
        *,
        import_metadata: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to import an external file as a new design in Canva.

        The request format for this endpoint has an `application/octet-stream` body of
        bytes, and the information about the import is provided using an
        `Import-Metadata` header.

        Supported file types for imports are listed in
        [Design imports overview](https://www.canva.dev/docs/connect/api-reference/design-imports/#supported-file-types).

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of design import jobs created with
        this API using the
        [Get design import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/get-design-import-job/).

        </Note>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Import-Metadata": str(import_metadata), **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return await self._post(
            "/v1/imports",
            body=await async_read_file_content(body),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportCreateResponse,
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
    ) -> ImportRetrieveResponse:
        """
        Gets the result of a design import job created using the
        [Create design import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/create-design-import-job/).

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
            f"/v1/imports/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportRetrieveResponse,
        )


class ImportsResourceWithRawResponse:
    def __init__(self, imports: ImportsResource) -> None:
        self._imports = imports

        self.create = to_raw_response_wrapper(
            imports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            imports.retrieve,
        )


class AsyncImportsResourceWithRawResponse:
    def __init__(self, imports: AsyncImportsResource) -> None:
        self._imports = imports

        self.create = async_to_raw_response_wrapper(
            imports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            imports.retrieve,
        )


class ImportsResourceWithStreamingResponse:
    def __init__(self, imports: ImportsResource) -> None:
        self._imports = imports

        self.create = to_streamed_response_wrapper(
            imports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            imports.retrieve,
        )


class AsyncImportsResourceWithStreamingResponse:
    def __init__(self, imports: AsyncImportsResource) -> None:
        self._imports = imports

        self.create = async_to_streamed_response_wrapper(
            imports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            imports.retrieve,
        )
