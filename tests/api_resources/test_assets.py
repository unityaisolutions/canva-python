# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import AssetUpdateResponse, AssetRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        asset = client.assets.retrieve(
            "assetId",
        )
        assert_matches_type(AssetRetrieveResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.assets.with_raw_response.retrieve(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetRetrieveResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.assets.with_streaming_response.retrieve(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetRetrieveResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Canva) -> None:
        asset = client.assets.update(
            asset_id="assetId",
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Canva) -> None:
        asset = client.assets.update(
            asset_id="assetId",
            name="My Awesome Upload",
            tags=["image", "holiday", "best day ever"],
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Canva) -> None:
        response = client.assets.with_raw_response.update(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Canva) -> None:
        with client.assets.with_streaming_response.update(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetUpdateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.update(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Canva) -> None:
        asset = client.assets.delete(
            "assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Canva) -> None:
        response = client.assets.with_raw_response.delete(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Canva) -> None:
        with client.assets.with_streaming_response.delete(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.with_raw_response.delete(
                "",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        asset = await async_client.assets.retrieve(
            "assetId",
        )
        assert_matches_type(AssetRetrieveResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.assets.with_raw_response.retrieve(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetRetrieveResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.assets.with_streaming_response.retrieve(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetRetrieveResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCanva) -> None:
        asset = await async_client.assets.update(
            asset_id="assetId",
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCanva) -> None:
        asset = await async_client.assets.update(
            asset_id="assetId",
            name="My Awesome Upload",
            tags=["image", "holiday", "best day ever"],
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCanva) -> None:
        response = await async_client.assets.with_raw_response.update(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCanva) -> None:
        async with async_client.assets.with_streaming_response.update(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetUpdateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.update(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCanva) -> None:
        asset = await async_client.assets.delete(
            "assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCanva) -> None:
        response = await async_client.assets.with_raw_response.delete(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCanva) -> None:
        async with async_client.assets.with_streaming_response.delete(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.with_raw_response.delete(
                "",
            )
