# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from tests.utils import assert_matches_type
from canva.types.users import MeRetrieveResponse, MeRetrieveProfileResponse, MeListCapabilitiesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        me = client.users.me.retrieve()
        assert_matches_type(MeRetrieveResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.users.me.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeRetrieveResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.users.me.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeRetrieveResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_capabilities(self, client: Canva) -> None:
        me = client.users.me.list_capabilities()
        assert_matches_type(MeListCapabilitiesResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_capabilities(self, client: Canva) -> None:
        response = client.users.me.with_raw_response.list_capabilities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeListCapabilitiesResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_capabilities(self, client: Canva) -> None:
        with client.users.me.with_streaming_response.list_capabilities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeListCapabilitiesResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_profile(self, client: Canva) -> None:
        me = client.users.me.retrieve_profile()
        assert_matches_type(MeRetrieveProfileResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_profile(self, client: Canva) -> None:
        response = client.users.me.with_raw_response.retrieve_profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeRetrieveProfileResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_profile(self, client: Canva) -> None:
        with client.users.me.with_streaming_response.retrieve_profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeRetrieveProfileResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        me = await async_client.users.me.retrieve()
        assert_matches_type(MeRetrieveResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.users.me.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeRetrieveResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.users.me.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeRetrieveResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_capabilities(self, async_client: AsyncCanva) -> None:
        me = await async_client.users.me.list_capabilities()
        assert_matches_type(MeListCapabilitiesResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_capabilities(self, async_client: AsyncCanva) -> None:
        response = await async_client.users.me.with_raw_response.list_capabilities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeListCapabilitiesResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_capabilities(self, async_client: AsyncCanva) -> None:
        async with async_client.users.me.with_streaming_response.list_capabilities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeListCapabilitiesResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_profile(self, async_client: AsyncCanva) -> None:
        me = await async_client.users.me.retrieve_profile()
        assert_matches_type(MeRetrieveProfileResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_profile(self, async_client: AsyncCanva) -> None:
        response = await async_client.users.me.with_raw_response.retrieve_profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeRetrieveProfileResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_profile(self, async_client: AsyncCanva) -> None:
        async with async_client.users.me.with_streaming_response.retrieve_profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeRetrieveProfileResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True
