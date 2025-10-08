# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import SortByType, OwnershipType, brand_template_list_params
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
from ..types.sort_by_type import SortByType
from ..types.ownership_type import OwnershipType
from ..types.brand_template_list_response import BrandTemplateListResponse
from ..types.brand_template_retrieve_response import BrandTemplateRetrieveResponse
from ..types.brand_template_retrieve_dataset_response import BrandTemplateRetrieveDatasetResponse

__all__ = ["BrandTemplatesResource", "AsyncBrandTemplatesResource"]


class BrandTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return BrandTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return BrandTemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        brand_template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandTemplateRetrieveResponse:
        """<Warning>

        Soon, all brand template IDs will be updated to a new format.

        If your
        integration stores brand template IDs, you'll need to migrate to use the new
        IDs. After we implement this change, you'll have 6 months to migrate before the
        old IDs are removed.

        </Warning>

        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Retrieves the metadata for a brand template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_template_id:
            raise ValueError(f"Expected a non-empty value for `brand_template_id` but received {brand_template_id!r}")
        return self._get(
            f"/v1/brand-templates/{brand_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandTemplateRetrieveResponse,
        )

    def list(
        self,
        *,
        continuation: str | Omit = omit,
        dataset: Literal["any", "non_empty"] | Omit = omit,
        ownership: OwnershipType | Omit = omit,
        query: str | Omit = omit,
        sort_by: SortByType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandTemplateListResponse:
        """<Warning>

        Soon, all brand template IDs will be updated to a new format.

        If your
        integration stores brand template IDs, you'll need to migrate to use the new
        IDs. After we implement this change, you'll have 6 months to migrate before the
        old IDs are removed.

        </Warning>

        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Get a list of the
        [brand templates](https://www.canva.com/help/publish-team-template/) the user
        has access to.

        Args:
          continuation: If the success response contains a continuation token, the user has access to
              more brand templates you can list. You can use this token as a query parameter
              and retrieve more templates from the list, for example
              `/v1/brand-templates?continuation={continuation}`. To retrieve all the brand
              templates available to the user, you might need to make multiple requests.

          dataset: Filter the list of brand templates based on the brand templates' dataset
              definitions. Brand templates with dataset definitions are mainly used with the
              [Autofill APIs](https://www.canva.dev/docs/connect/api-reference/autofills/).

              - `any` - Brand templates with and without dataset definitions.
              - `non_empty` - Brand templates with one or more data fields defined.

          ownership: Filter the list of brand templates based on the user's ownership of the brand
              templates.

          query: Lets you search the brand templates available to the user using a search term or
              terms.

          sort_by: Sort the list of brand templates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/brand-templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuation": continuation,
                        "dataset": dataset,
                        "ownership": ownership,
                        "query": query,
                        "sort_by": sort_by,
                    },
                    brand_template_list_params.BrandTemplateListParams,
                ),
            ),
            cast_to=BrandTemplateListResponse,
        )

    def retrieve_dataset(
        self,
        brand_template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandTemplateRetrieveDatasetResponse:
        """<Warning>

        Soon, all brand template IDs will be updated to a new format.

        If your
        integration stores brand template IDs, you'll need to migrate to use the new
        IDs. After we implement this change, you'll have 6 months to migrate before the
        old IDs are removed.

        </Warning>

        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Gets the dataset definition of a brand template. If the brand template contains
        autofill data fields, this API returns an object with the data field names and
        the type of data they accept.

        Available data field types include:

        - Images
        - Text
        - Charts

        You can autofill a brand template using the
        [Create a design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/).

        WARNING: Chart data fields are a
        [preview feature](https://www.canva.dev/docs/connect/#preview-apis). There might
        be unannounced breaking changes to this feature which won't produce a new API
        version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_template_id:
            raise ValueError(f"Expected a non-empty value for `brand_template_id` but received {brand_template_id!r}")
        return self._get(
            f"/v1/brand-templates/{brand_template_id}/dataset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandTemplateRetrieveDatasetResponse,
        )


class AsyncBrandTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncBrandTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        brand_template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandTemplateRetrieveResponse:
        """<Warning>

        Soon, all brand template IDs will be updated to a new format.

        If your
        integration stores brand template IDs, you'll need to migrate to use the new
        IDs. After we implement this change, you'll have 6 months to migrate before the
        old IDs are removed.

        </Warning>

        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Retrieves the metadata for a brand template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_template_id:
            raise ValueError(f"Expected a non-empty value for `brand_template_id` but received {brand_template_id!r}")
        return await self._get(
            f"/v1/brand-templates/{brand_template_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandTemplateRetrieveResponse,
        )

    async def list(
        self,
        *,
        continuation: str | Omit = omit,
        dataset: Literal["any", "non_empty"] | Omit = omit,
        ownership: OwnershipType | Omit = omit,
        query: str | Omit = omit,
        sort_by: SortByType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandTemplateListResponse:
        """<Warning>

        Soon, all brand template IDs will be updated to a new format.

        If your
        integration stores brand template IDs, you'll need to migrate to use the new
        IDs. After we implement this change, you'll have 6 months to migrate before the
        old IDs are removed.

        </Warning>

        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Get a list of the
        [brand templates](https://www.canva.com/help/publish-team-template/) the user
        has access to.

        Args:
          continuation: If the success response contains a continuation token, the user has access to
              more brand templates you can list. You can use this token as a query parameter
              and retrieve more templates from the list, for example
              `/v1/brand-templates?continuation={continuation}`. To retrieve all the brand
              templates available to the user, you might need to make multiple requests.

          dataset: Filter the list of brand templates based on the brand templates' dataset
              definitions. Brand templates with dataset definitions are mainly used with the
              [Autofill APIs](https://www.canva.dev/docs/connect/api-reference/autofills/).

              - `any` - Brand templates with and without dataset definitions.
              - `non_empty` - Brand templates with one or more data fields defined.

          ownership: Filter the list of brand templates based on the user's ownership of the brand
              templates.

          query: Lets you search the brand templates available to the user using a search term or
              terms.

          sort_by: Sort the list of brand templates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/brand-templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continuation": continuation,
                        "dataset": dataset,
                        "ownership": ownership,
                        "query": query,
                        "sort_by": sort_by,
                    },
                    brand_template_list_params.BrandTemplateListParams,
                ),
            ),
            cast_to=BrandTemplateListResponse,
        )

    async def retrieve_dataset(
        self,
        brand_template_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandTemplateRetrieveDatasetResponse:
        """<Warning>

        Soon, all brand template IDs will be updated to a new format.

        If your
        integration stores brand template IDs, you'll need to migrate to use the new
        IDs. After we implement this change, you'll have 6 months to migrate before the
        old IDs are removed.

        </Warning>

        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Gets the dataset definition of a brand template. If the brand template contains
        autofill data fields, this API returns an object with the data field names and
        the type of data they accept.

        Available data field types include:

        - Images
        - Text
        - Charts

        You can autofill a brand template using the
        [Create a design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/).

        WARNING: Chart data fields are a
        [preview feature](https://www.canva.dev/docs/connect/#preview-apis). There might
        be unannounced breaking changes to this feature which won't produce a new API
        version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_template_id:
            raise ValueError(f"Expected a non-empty value for `brand_template_id` but received {brand_template_id!r}")
        return await self._get(
            f"/v1/brand-templates/{brand_template_id}/dataset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandTemplateRetrieveDatasetResponse,
        )


class BrandTemplatesResourceWithRawResponse:
    def __init__(self, brand_templates: BrandTemplatesResource) -> None:
        self._brand_templates = brand_templates

        self.retrieve = to_raw_response_wrapper(
            brand_templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            brand_templates.list,
        )
        self.retrieve_dataset = to_raw_response_wrapper(
            brand_templates.retrieve_dataset,
        )


class AsyncBrandTemplatesResourceWithRawResponse:
    def __init__(self, brand_templates: AsyncBrandTemplatesResource) -> None:
        self._brand_templates = brand_templates

        self.retrieve = async_to_raw_response_wrapper(
            brand_templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            brand_templates.list,
        )
        self.retrieve_dataset = async_to_raw_response_wrapper(
            brand_templates.retrieve_dataset,
        )


class BrandTemplatesResourceWithStreamingResponse:
    def __init__(self, brand_templates: BrandTemplatesResource) -> None:
        self._brand_templates = brand_templates

        self.retrieve = to_streamed_response_wrapper(
            brand_templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            brand_templates.list,
        )
        self.retrieve_dataset = to_streamed_response_wrapper(
            brand_templates.retrieve_dataset,
        )


class AsyncBrandTemplatesResourceWithStreamingResponse:
    def __init__(self, brand_templates: AsyncBrandTemplatesResource) -> None:
        self._brand_templates = brand_templates

        self.retrieve = async_to_streamed_response_wrapper(
            brand_templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            brand_templates.list,
        )
        self.retrieve_dataset = async_to_streamed_response_wrapper(
            brand_templates.retrieve_dataset,
        )
