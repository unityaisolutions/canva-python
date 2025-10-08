# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import ResizeCreateResponse, ResizeRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResizes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        resize = client.resizes.create(
            design_id="DAGirp_1ZUA",
            design_type={
                "height": 1500,
                "type": "custom",
                "width": 1000,
            },
        )
        assert_matches_type(ResizeCreateResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.resizes.with_raw_response.create(
            design_id="DAGirp_1ZUA",
            design_type={
                "height": 1500,
                "type": "custom",
                "width": 1000,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resize = response.parse()
        assert_matches_type(ResizeCreateResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.resizes.with_streaming_response.create(
            design_id="DAGirp_1ZUA",
            design_type={
                "height": 1500,
                "type": "custom",
                "width": 1000,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resize = response.parse()
            assert_matches_type(ResizeCreateResponse, resize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        resize = client.resizes.retrieve(
            "jobId",
        )
        assert_matches_type(ResizeRetrieveResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.resizes.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resize = response.parse()
        assert_matches_type(ResizeRetrieveResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.resizes.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resize = response.parse()
            assert_matches_type(ResizeRetrieveResponse, resize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.resizes.with_raw_response.retrieve(
                "",
            )


class TestAsyncResizes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        resize = await async_client.resizes.create(
            design_id="DAGirp_1ZUA",
            design_type={
                "height": 1500,
                "type": "custom",
                "width": 1000,
            },
        )
        assert_matches_type(ResizeCreateResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.resizes.with_raw_response.create(
            design_id="DAGirp_1ZUA",
            design_type={
                "height": 1500,
                "type": "custom",
                "width": 1000,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resize = await response.parse()
        assert_matches_type(ResizeCreateResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.resizes.with_streaming_response.create(
            design_id="DAGirp_1ZUA",
            design_type={
                "height": 1500,
                "type": "custom",
                "width": 1000,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resize = await response.parse()
            assert_matches_type(ResizeCreateResponse, resize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        resize = await async_client.resizes.retrieve(
            "jobId",
        )
        assert_matches_type(ResizeRetrieveResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.resizes.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resize = await response.parse()
        assert_matches_type(ResizeRetrieveResponse, resize, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.resizes.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resize = await response.parse()
            assert_matches_type(ResizeRetrieveResponse, resize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.resizes.with_raw_response.retrieve(
                "",
            )
