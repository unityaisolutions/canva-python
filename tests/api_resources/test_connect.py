# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import ConnectRetrieveKeysResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_keys(self, client: Canva) -> None:
        connect = client.connect.retrieve_keys()
        assert_matches_type(ConnectRetrieveKeysResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_keys(self, client: Canva) -> None:
        response = client.connect.with_raw_response.retrieve_keys()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert_matches_type(ConnectRetrieveKeysResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_keys(self, client: Canva) -> None:
        with client.connect.with_streaming_response.retrieve_keys() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert_matches_type(ConnectRetrieveKeysResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_keys(self, async_client: AsyncCanva) -> None:
        connect = await async_client.connect.retrieve_keys()
        assert_matches_type(ConnectRetrieveKeysResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_keys(self, async_client: AsyncCanva) -> None:
        response = await async_client.connect.with_raw_response.retrieve_keys()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert_matches_type(ConnectRetrieveKeysResponse, connect, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_keys(self, async_client: AsyncCanva) -> None:
        async with async_client.connect.with_streaming_response.retrieve_keys() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert_matches_type(ConnectRetrieveKeysResponse, connect, path=["response"])

        assert cast(Any, response.is_closed) is True
