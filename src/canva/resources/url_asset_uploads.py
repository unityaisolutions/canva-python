# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import url_asset_upload_create_params
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
from ..types.url_asset_upload_create_response import URLAssetUploadCreateResponse
from ..types.url_asset_upload_retrieve_response import URLAssetUploadRetrieveResponse

__all__ = ["URLAssetUploadsResource", "AsyncURLAssetUploadsResource"]


class URLAssetUploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLAssetUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return URLAssetUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLAssetUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return URLAssetUploadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLAssetUploadCreateResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to upload an asset from a URL to the user's content library. Supported file
        types for assets are listed in the
        [Assets API overview](https://www.canva.dev/docs/connect/api-reference/assets/).

        <Note>
         Uploading a video asset from a URL is limited to a maximum 100MB file size. For importing larger video files, use the [Create asset upload job API](https://www.canva.dev/docs/connect/api-reference/assets/create-asset-upload-job/).
        </Note>

        <Note>
        For more information on the workflow for using asynchronous jobs, see [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints). You can check the status and get the results of asset upload jobs created with this API using the [Get asset upload job via URL API](https://www.canva.dev/docs/connect/api-reference/assets/get-url-asset-upload-job/).
        </Note>

        Args:
          name: A name for the asset.

          url: The URL of the file to import. This URL must be accessible from the internet and
              be publicly available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/url-asset-uploads",
            body=maybe_transform(
                {
                    "name": name,
                    "url": url,
                },
                url_asset_upload_create_params.URLAssetUploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLAssetUploadCreateResponse,
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
    ) -> URLAssetUploadRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Get the result of an asset upload job that was created using the
        [Create asset upload job via URL API](https://www.canva.dev/docs/connect/api-reference/assets/create-url-asset-upload-job/).

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
            f"/v1/url-asset-uploads/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLAssetUploadRetrieveResponse,
        )


class AsyncURLAssetUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLAssetUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLAssetUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLAssetUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncURLAssetUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLAssetUploadCreateResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to upload an asset from a URL to the user's content library. Supported file
        types for assets are listed in the
        [Assets API overview](https://www.canva.dev/docs/connect/api-reference/assets/).

        <Note>
         Uploading a video asset from a URL is limited to a maximum 100MB file size. For importing larger video files, use the [Create asset upload job API](https://www.canva.dev/docs/connect/api-reference/assets/create-asset-upload-job/).
        </Note>

        <Note>
        For more information on the workflow for using asynchronous jobs, see [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints). You can check the status and get the results of asset upload jobs created with this API using the [Get asset upload job via URL API](https://www.canva.dev/docs/connect/api-reference/assets/get-url-asset-upload-job/).
        </Note>

        Args:
          name: A name for the asset.

          url: The URL of the file to import. This URL must be accessible from the internet and
              be publicly available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/url-asset-uploads",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "url": url,
                },
                url_asset_upload_create_params.URLAssetUploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLAssetUploadCreateResponse,
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
    ) -> URLAssetUploadRetrieveResponse:
        """<Warning>

        This API is currently provided as a preview.

        Be aware of the following:

        - There might be unannounced breaking changes.
        - Any breaking changes to preview APIs won't produce a new
          [API version](https://www.canva.dev/docs/connect/versions/).
        - Public integrations that use preview APIs will not pass the review process,
          and can't be made available to all Canva users.

        </Warning>

        Get the result of an asset upload job that was created using the
        [Create asset upload job via URL API](https://www.canva.dev/docs/connect/api-reference/assets/create-url-asset-upload-job/).

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
            f"/v1/url-asset-uploads/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLAssetUploadRetrieveResponse,
        )


class URLAssetUploadsResourceWithRawResponse:
    def __init__(self, url_asset_uploads: URLAssetUploadsResource) -> None:
        self._url_asset_uploads = url_asset_uploads

        self.create = to_raw_response_wrapper(
            url_asset_uploads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            url_asset_uploads.retrieve,
        )


class AsyncURLAssetUploadsResourceWithRawResponse:
    def __init__(self, url_asset_uploads: AsyncURLAssetUploadsResource) -> None:
        self._url_asset_uploads = url_asset_uploads

        self.create = async_to_raw_response_wrapper(
            url_asset_uploads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            url_asset_uploads.retrieve,
        )


class URLAssetUploadsResourceWithStreamingResponse:
    def __init__(self, url_asset_uploads: URLAssetUploadsResource) -> None:
        self._url_asset_uploads = url_asset_uploads

        self.create = to_streamed_response_wrapper(
            url_asset_uploads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            url_asset_uploads.retrieve,
        )


class AsyncURLAssetUploadsResourceWithStreamingResponse:
    def __init__(self, url_asset_uploads: AsyncURLAssetUploadsResource) -> None:
        self._url_asset_uploads = url_asset_uploads

        self.create = async_to_streamed_response_wrapper(
            url_asset_uploads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            url_asset_uploads.retrieve,
        )
