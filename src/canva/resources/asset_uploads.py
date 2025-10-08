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
from ..types.asset_upload_create_response import AssetUploadCreateResponse
from ..types.asset_upload_retrieve_response import AssetUploadRetrieveResponse

__all__ = ["AssetUploadsResource", "AsyncAssetUploadsResource"]


class AssetUploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AssetUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AssetUploadsResourceWithStreamingResponse(self)

    def create(
        self,
        body: FileContent,
        *,
        asset_upload_metadata: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to upload an asset to the user's content library. Supported file types for
        assets are listed in the
        [Assets API overview](https://www.canva.dev/docs/connect/api-reference/assets/).

        The request format for this endpoint is an `application/octet-stream` body of
        bytes. Attach information about the upload using an `Asset-Upload-Metadata`
        header.

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of asset upload jobs created with
        this API using the
        [Get asset upload job API](https://www.canva.dev/docs/connect/api-reference/assets/get-asset-upload-job/).

        </Note>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Asset-Upload-Metadata": str(asset_upload_metadata), **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return self._post(
            "/v1/asset-uploads",
            body=read_file_content(body),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadCreateResponse,
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
    ) -> AssetUploadRetrieveResponse:
        """
        Get the result of an asset upload job that was created using the
        [Create asset upload job API](https://www.canva.dev/docs/connect/api-reference/assets/create-asset-upload-job/).

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
            f"/v1/asset-uploads/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadRetrieveResponse,
        )


class AsyncAssetUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncAssetUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        body: FileContent,
        *,
        asset_upload_metadata: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadCreateResponse:
        """
        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to upload an asset to the user's content library. Supported file types for
        assets are listed in the
        [Assets API overview](https://www.canva.dev/docs/connect/api-reference/assets/).

        The request format for this endpoint is an `application/octet-stream` body of
        bytes. Attach information about the upload using an `Asset-Upload-Metadata`
        header.

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of asset upload jobs created with
        this API using the
        [Get asset upload job API](https://www.canva.dev/docs/connect/api-reference/assets/get-asset-upload-job/).

        </Note>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Asset-Upload-Metadata": str(asset_upload_metadata), **(extra_headers or {})}
        extra_headers["Content-Type"] = "application/octet-stream"
        return await self._post(
            "/v1/asset-uploads",
            body=await async_read_file_content(body),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadCreateResponse,
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
    ) -> AssetUploadRetrieveResponse:
        """
        Get the result of an asset upload job that was created using the
        [Create asset upload job API](https://www.canva.dev/docs/connect/api-reference/assets/create-asset-upload-job/).

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
            f"/v1/asset-uploads/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadRetrieveResponse,
        )


class AssetUploadsResourceWithRawResponse:
    def __init__(self, asset_uploads: AssetUploadsResource) -> None:
        self._asset_uploads = asset_uploads

        self.create = to_raw_response_wrapper(
            asset_uploads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            asset_uploads.retrieve,
        )


class AsyncAssetUploadsResourceWithRawResponse:
    def __init__(self, asset_uploads: AsyncAssetUploadsResource) -> None:
        self._asset_uploads = asset_uploads

        self.create = async_to_raw_response_wrapper(
            asset_uploads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            asset_uploads.retrieve,
        )


class AssetUploadsResourceWithStreamingResponse:
    def __init__(self, asset_uploads: AssetUploadsResource) -> None:
        self._asset_uploads = asset_uploads

        self.create = to_streamed_response_wrapper(
            asset_uploads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            asset_uploads.retrieve,
        )


class AsyncAssetUploadsResourceWithStreamingResponse:
    def __init__(self, asset_uploads: AsyncAssetUploadsResource) -> None:
        self._asset_uploads = asset_uploads

        self.create = async_to_streamed_response_wrapper(
            asset_uploads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            asset_uploads.retrieve,
        )
