# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import asset_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.asset_update_response import AssetUpdateResponse
from ..types.asset_retrieve_response import AssetRetrieveResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetRetrieveResponse:
        """
        You can retrieve the metadata of an asset by specifying its `assetId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            f"/v1/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetRetrieveResponse,
        )

    def update(
        self,
        asset_id: str,
        *,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUpdateResponse:
        """
        You can update the name and tags of an asset by specifying its `assetId`.
        Updating the tags replaces all existing tags of the asset.

        Args:
          name: The name of the asset. This is shown in the Canva UI. When this field is
              undefined or empty, nothing is updated.

          tags: The replacement tags for the asset. When this field is undefined, nothing is
              updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._patch(
            f"/v1/assets/{asset_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUpdateResponse,
        )

    def delete(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You can delete an asset by specifying its `assetId`.

        This operation mirrors the
        behavior in the Canva UI. Deleting an item moves it to the trash. Deleting an
        asset doesn't remove it from designs that already use it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetRetrieveResponse:
        """
        You can retrieve the metadata of an asset by specifying its `assetId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            f"/v1/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetRetrieveResponse,
        )

    async def update(
        self,
        asset_id: str,
        *,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUpdateResponse:
        """
        You can update the name and tags of an asset by specifying its `assetId`.
        Updating the tags replaces all existing tags of the asset.

        Args:
          name: The name of the asset. This is shown in the Canva UI. When this field is
              undefined or empty, nothing is updated.

          tags: The replacement tags for the asset. When this field is undefined, nothing is
              updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._patch(
            f"/v1/assets/{asset_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUpdateResponse,
        )

    async def delete(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """You can delete an asset by specifying its `assetId`.

        This operation mirrors the
        behavior in the Canva UI. Deleting an item moves it to the trash. Deleting an
        asset doesn't remove it from designs that already use it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/assets/{asset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.retrieve = to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.retrieve = async_to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.retrieve = to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.retrieve = async_to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )
