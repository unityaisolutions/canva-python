# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import autofill_create_params
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
from ..types.autofill_create_response import AutofillCreateResponse
from ..types.autofill_retrieve_response import AutofillRetrieveResponse

__all__ = ["AutofillsResource", "AsyncAutofillsResource"]


class AutofillsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutofillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AutofillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutofillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AutofillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        brand_template_id: str,
        data: Dict[str, autofill_create_params.Data],
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutofillCreateResponse:
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

        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to autofill a Canva design using a brand template and input data.

        To get a list of input data fields, use the
        [Get brand template dataset API](https://www.canva.dev/docs/connect/api-reference/brand-templates/get-brand-template-dataset/).

        Available data field types to autofill include:

        - Images
        - Text
        - Charts

          WARNING: Chart data fields are a
          [preview feature](https://www.canva.dev/docs/connect/#preview-apis). There
          might be unannounced breaking changes to this feature which won't produce a
          new API version.

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of autofill jobs created with this
        API using the
        [Get design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/get-design-autofill-job/).

        </Note>

        Args:
          brand_template_id: ID of the input brand template.

          data: Data object containing the data fields and values to autofill.

          title: Title to use for the autofilled design.

              If no design title is provided, the autofilled design will have the same title
              as the brand template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/autofills",
            body=maybe_transform(
                {
                    "brand_template_id": brand_template_id,
                    "data": data,
                    "title": title,
                },
                autofill_create_params.AutofillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutofillCreateResponse,
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
    ) -> AutofillRetrieveResponse:
        """
        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Get the result of a design autofill job that was created using the
        [Create design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/).

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
            f"/v1/autofills/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutofillRetrieveResponse,
        )


class AsyncAutofillsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutofillsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutofillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutofillsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/canva-python#with_streaming_response
        """
        return AsyncAutofillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        brand_template_id: str,
        data: Dict[str, autofill_create_params.Data],
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutofillCreateResponse:
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

        Starts a new
        [asynchronous job](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints)
        to autofill a Canva design using a brand template and input data.

        To get a list of input data fields, use the
        [Get brand template dataset API](https://www.canva.dev/docs/connect/api-reference/brand-templates/get-brand-template-dataset/).

        Available data field types to autofill include:

        - Images
        - Text
        - Charts

          WARNING: Chart data fields are a
          [preview feature](https://www.canva.dev/docs/connect/#preview-apis). There
          might be unannounced breaking changes to this feature which won't produce a
          new API version.

        <Note>

        For more information on the workflow for using asynchronous jobs, see
        [API requests and responses](https://www.canva.dev/docs/connect/api-requests-responses/#asynchronous-job-endpoints).
        You can check the status and get the results of autofill jobs created with this
        API using the
        [Get design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/get-design-autofill-job/).

        </Note>

        Args:
          brand_template_id: ID of the input brand template.

          data: Data object containing the data fields and values to autofill.

          title: Title to use for the autofilled design.

              If no design title is provided, the autofilled design will have the same title
              as the brand template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/autofills",
            body=await async_maybe_transform(
                {
                    "brand_template_id": brand_template_id,
                    "data": data,
                    "title": title,
                },
                autofill_create_params.AutofillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutofillCreateResponse,
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
    ) -> AutofillRetrieveResponse:
        """
        <Note>

        To use this API, your integration must act on behalf of a user that's a member
        of a [Canva Enterprise](https://www.canva.com/enterprise/) organization.

        </Note>

        Get the result of a design autofill job that was created using the
        [Create design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/).

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
            f"/v1/autofills/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutofillRetrieveResponse,
        )


class AutofillsResourceWithRawResponse:
    def __init__(self, autofills: AutofillsResource) -> None:
        self._autofills = autofills

        self.create = to_raw_response_wrapper(
            autofills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            autofills.retrieve,
        )


class AsyncAutofillsResourceWithRawResponse:
    def __init__(self, autofills: AsyncAutofillsResource) -> None:
        self._autofills = autofills

        self.create = async_to_raw_response_wrapper(
            autofills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            autofills.retrieve,
        )


class AutofillsResourceWithStreamingResponse:
    def __init__(self, autofills: AutofillsResource) -> None:
        self._autofills = autofills

        self.create = to_streamed_response_wrapper(
            autofills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            autofills.retrieve,
        )


class AsyncAutofillsResourceWithStreamingResponse:
    def __init__(self, autofills: AsyncAutofillsResource) -> None:
        self._autofills = autofills

        self.create = async_to_streamed_response_wrapper(
            autofills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            autofills.retrieve,
        )
