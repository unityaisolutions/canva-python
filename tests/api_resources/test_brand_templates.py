# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import (
    BrandTemplateListResponse,
    BrandTemplateRetrieveResponse,
    BrandTemplateRetrieveDatasetResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrandTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        brand_template = client.brand_templates.retrieve(
            "brandTemplateId",
        )
        assert_matches_type(BrandTemplateRetrieveResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.brand_templates.with_raw_response.retrieve(
            "brandTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_template = response.parse()
        assert_matches_type(BrandTemplateRetrieveResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.brand_templates.with_streaming_response.retrieve(
            "brandTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_template = response.parse()
            assert_matches_type(BrandTemplateRetrieveResponse, brand_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_template_id` but received ''"):
            client.brand_templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Canva) -> None:
        brand_template = client.brand_templates.list()
        assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Canva) -> None:
        brand_template = client.brand_templates.list(
            continuation="continuation",
            dataset="any",
            ownership="any",
            query="query",
            sort_by="relevance",
        )
        assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Canva) -> None:
        response = client.brand_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_template = response.parse()
        assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Canva) -> None:
        with client.brand_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_template = response.parse()
            assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_dataset(self, client: Canva) -> None:
        brand_template = client.brand_templates.retrieve_dataset(
            "brandTemplateId",
        )
        assert_matches_type(BrandTemplateRetrieveDatasetResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_dataset(self, client: Canva) -> None:
        response = client.brand_templates.with_raw_response.retrieve_dataset(
            "brandTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_template = response.parse()
        assert_matches_type(BrandTemplateRetrieveDatasetResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_dataset(self, client: Canva) -> None:
        with client.brand_templates.with_streaming_response.retrieve_dataset(
            "brandTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_template = response.parse()
            assert_matches_type(BrandTemplateRetrieveDatasetResponse, brand_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_dataset(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_template_id` but received ''"):
            client.brand_templates.with_raw_response.retrieve_dataset(
                "",
            )


class TestAsyncBrandTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        brand_template = await async_client.brand_templates.retrieve(
            "brandTemplateId",
        )
        assert_matches_type(BrandTemplateRetrieveResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.brand_templates.with_raw_response.retrieve(
            "brandTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_template = await response.parse()
        assert_matches_type(BrandTemplateRetrieveResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.brand_templates.with_streaming_response.retrieve(
            "brandTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_template = await response.parse()
            assert_matches_type(BrandTemplateRetrieveResponse, brand_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_template_id` but received ''"):
            await async_client.brand_templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCanva) -> None:
        brand_template = await async_client.brand_templates.list()
        assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCanva) -> None:
        brand_template = await async_client.brand_templates.list(
            continuation="continuation",
            dataset="any",
            ownership="any",
            query="query",
            sort_by="relevance",
        )
        assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCanva) -> None:
        response = await async_client.brand_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_template = await response.parse()
        assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCanva) -> None:
        async with async_client.brand_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_template = await response.parse()
            assert_matches_type(BrandTemplateListResponse, brand_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_dataset(self, async_client: AsyncCanva) -> None:
        brand_template = await async_client.brand_templates.retrieve_dataset(
            "brandTemplateId",
        )
        assert_matches_type(BrandTemplateRetrieveDatasetResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_dataset(self, async_client: AsyncCanva) -> None:
        response = await async_client.brand_templates.with_raw_response.retrieve_dataset(
            "brandTemplateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand_template = await response.parse()
        assert_matches_type(BrandTemplateRetrieveDatasetResponse, brand_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_dataset(self, async_client: AsyncCanva) -> None:
        async with async_client.brand_templates.with_streaming_response.retrieve_dataset(
            "brandTemplateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand_template = await response.parse()
            assert_matches_type(BrandTemplateRetrieveDatasetResponse, brand_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_dataset(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_template_id` but received ''"):
            await async_client.brand_templates.with_raw_response.retrieve_dataset(
                "",
            )
