# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import url_import_create_params
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
from ..types.url_import_create_response import URLImportCreateResponse
from ..types.url_import_retrieve_response import URLImportRetrieveResponse

__all__ = ["URLImportsResource", "AsyncURLImportsResource"]


class URLImportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return URLImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return URLImportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        title: str,
        url: str,
        mime_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLImportCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to import an external file from a URL as a new design in Canva.

        Supported file types for imports are listed in
        [Design imports overview](https://www.canva.dev/docs/connect/api-reference/design-imports/#supported-file-types).

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of design import jobs created with
        this API using the
        [Get URL import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/get-url-import-job/).

        </Note>

        Args:
          title: A title for the design.

          url: The URL of the file to import. This URL must be accessible from the internet and
              be publicly available.

          mime_type: The MIME type of the file being imported. If not provided, Canva attempts to
              automatically detect the type of the file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/url-imports",
            body=maybe_transform(
                {
                    "title": title,
                    "url": url,
                    "mime_type": mime_type,
                },
                url_import_create_params.URLImportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLImportCreateResponse,
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
    ) -> URLImportRetrieveResponse:
        """
        Gets the result of a URL import job created using the
        [Create URL import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/create-url-import-job/).

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
            f"/v1/url-imports/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLImportRetrieveResponse,
        )


class AsyncURLImportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLImportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLImportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLImportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncURLImportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        title: str,
        url: str,
        mime_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLImportCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to import an external file from a URL as a new design in Canva.

        Supported file types for imports are listed in
        [Design imports overview](https://www.canva.dev/docs/connect/api-reference/design-imports/#supported-file-types).

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of design import jobs created with
        this API using the
        [Get URL import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/get-url-import-job/).

        </Note>

        Args:
          title: A title for the design.

          url: The URL of the file to import. This URL must be accessible from the internet and
              be publicly available.

          mime_type: The MIME type of the file being imported. If not provided, Canva attempts to
              automatically detect the type of the file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/url-imports",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "url": url,
                    "mime_type": mime_type,
                },
                url_import_create_params.URLImportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLImportCreateResponse,
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
    ) -> URLImportRetrieveResponse:
        """
        Gets the result of a URL import job created using the
        [Create URL import job API](https://www.canva.dev/docs/connect/api-reference/design-imports/create-url-import-job/).

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
            f"/v1/url-imports/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLImportRetrieveResponse,
        )


class URLImportsResourceWithRawResponse:
    def __init__(self, url_imports: URLImportsResource) -> None:
        self._url_imports = url_imports

        self.create = to_raw_response_wrapper(
            url_imports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            url_imports.retrieve,
        )


class AsyncURLImportsResourceWithRawResponse:
    def __init__(self, url_imports: AsyncURLImportsResource) -> None:
        self._url_imports = url_imports

        self.create = async_to_raw_response_wrapper(
            url_imports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            url_imports.retrieve,
        )


class URLImportsResourceWithStreamingResponse:
    def __init__(self, url_imports: URLImportsResource) -> None:
        self._url_imports = url_imports

        self.create = to_streamed_response_wrapper(
            url_imports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            url_imports.retrieve,
        )


class AsyncURLImportsResourceWithStreamingResponse:
    def __init__(self, url_imports: AsyncURLImportsResource) -> None:
        self._url_imports = url_imports

        self.create = async_to_streamed_response_wrapper(
            url_imports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            url_imports.retrieve,
        )
