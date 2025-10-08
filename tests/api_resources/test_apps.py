# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import AppRetrieveJwksResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_jwks(self, client: Canva) -> None:
        app = client.apps.retrieve_jwks(
            "appId",
        )
        assert_matches_type(AppRetrieveJwksResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_jwks(self, client: Canva) -> None:
        response = client.apps.with_raw_response.retrieve_jwks(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppRetrieveJwksResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_jwks(self, client: Canva) -> None:
        with client.apps.with_streaming_response.retrieve_jwks(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppRetrieveJwksResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_jwks(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.apps.with_raw_response.retrieve_jwks(
                "",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_jwks(self, async_client: AsyncCanva) -> None:
        app = await async_client.apps.retrieve_jwks(
            "appId",
        )
        assert_matches_type(AppRetrieveJwksResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_jwks(self, async_client: AsyncCanva) -> None:
        response = await async_client.apps.with_raw_response.retrieve_jwks(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppRetrieveJwksResponse, app, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_jwks(self, async_client: AsyncCanva) -> None:
        async with async_client.apps.with_streaming_response.retrieve_jwks(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppRetrieveJwksResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_jwks(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.apps.with_raw_response.retrieve_jwks(
                "",
            )
