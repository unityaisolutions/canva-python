# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import (
    DesignListResponse,
    DesignCreateResponse,
    DesignRetrieveResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDesigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        design = client.designs.create()
        assert_matches_type(DesignCreateResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Canva) -> None:
        design = client.designs.create(
            asset_id="Msd59349ff",
            design_type={
                "name": "doc",
                "type": "preset",
            },
            title="My Holiday Presentation",
        )
        assert_matches_type(DesignCreateResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.designs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        design = response.parse()
        assert_matches_type(DesignCreateResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.designs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            design = response.parse()
            assert_matches_type(DesignCreateResponse, design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        design = client.designs.retrieve(
            "designId",
        )
        assert_matches_type(DesignRetrieveResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.designs.with_raw_response.retrieve(
            "designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        design = response.parse()
        assert_matches_type(DesignRetrieveResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.designs.with_streaming_response.retrieve(
            "designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            design = response.parse()
            assert_matches_type(DesignRetrieveResponse, design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Canva) -> None:
        design = client.designs.list()
        assert_matches_type(DesignListResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Canva) -> None:
        design = client.designs.list(
            continuation="continuation",
            ownership="any",
            query="query",
            sort_by="relevance",
        )
        assert_matches_type(DesignListResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Canva) -> None:
        response = client.designs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        design = response.parse()
        assert_matches_type(DesignListResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Canva) -> None:
        with client.designs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            design = response.parse()
            assert_matches_type(DesignListResponse, design, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDesigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        design = await async_client.designs.create()
        assert_matches_type(DesignCreateResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCanva) -> None:
        design = await async_client.designs.create(
            asset_id="Msd59349ff",
            design_type={
                "name": "doc",
                "type": "preset",
            },
            title="My Holiday Presentation",
        )
        assert_matches_type(DesignCreateResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        design = await response.parse()
        assert_matches_type(DesignCreateResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            design = await response.parse()
            assert_matches_type(DesignCreateResponse, design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        design = await async_client.designs.retrieve(
            "designId",
        )
        assert_matches_type(DesignRetrieveResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.with_raw_response.retrieve(
            "designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        design = await response.parse()
        assert_matches_type(DesignRetrieveResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.with_streaming_response.retrieve(
            "designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            design = await response.parse()
            assert_matches_type(DesignRetrieveResponse, design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCanva) -> None:
        design = await async_client.designs.list()
        assert_matches_type(DesignListResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCanva) -> None:
        design = await async_client.designs.list(
            continuation="continuation",
            ownership="any",
            query="query",
            sort_by="relevance",
        )
        assert_matches_type(DesignListResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        design = await response.parse()
        assert_matches_type(DesignListResponse, design, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            design = await response.parse()
            assert_matches_type(DesignListResponse, design, path=["response"])

        assert cast(Any, response.is_closed) is True
