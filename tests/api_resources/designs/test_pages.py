# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from tests.utils import assert_matches_type
from canva.types.designs import PageRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        page = client.designs.pages.retrieve(
            design_id="designId",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Canva) -> None:
        page = client.designs.pages.retrieve(
            design_id="designId",
            limit=1,
            offset=1,
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.designs.pages.with_raw_response.retrieve(
            design_id="designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.designs.pages.with_streaming_response.retrieve(
            design_id="designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.pages.with_raw_response.retrieve(
                design_id="",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        page = await async_client.designs.pages.retrieve(
            design_id="designId",
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCanva) -> None:
        page = await async_client.designs.pages.retrieve(
            design_id="designId",
            limit=1,
            offset=1,
        )
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.pages.with_raw_response.retrieve(
            design_id="designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(PageRetrieveResponse, page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.pages.with_streaming_response.retrieve(
            design_id="designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(PageRetrieveResponse, page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.pages.with_raw_response.retrieve(
                design_id="",
            )
