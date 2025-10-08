# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import AssetUploadCreateResponse, AssetUploadRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssetUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        asset_upload = client.asset_uploads.create(
            body=b"raw file contents",
            asset_upload_metadata={},
        )
        assert_matches_type(AssetUploadCreateResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.asset_uploads.with_raw_response.create(
            body=b"raw file contents",
            asset_upload_metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset_upload = response.parse()
        assert_matches_type(AssetUploadCreateResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.asset_uploads.with_streaming_response.create(
            body=b"raw file contents",
            asset_upload_metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset_upload = response.parse()
            assert_matches_type(AssetUploadCreateResponse, asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        asset_upload = client.asset_uploads.retrieve(
            "jobId",
        )
        assert_matches_type(AssetUploadRetrieveResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.asset_uploads.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset_upload = response.parse()
        assert_matches_type(AssetUploadRetrieveResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.asset_uploads.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset_upload = response.parse()
            assert_matches_type(AssetUploadRetrieveResponse, asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.asset_uploads.with_raw_response.retrieve(
                "",
            )


class TestAsyncAssetUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        asset_upload = await async_client.asset_uploads.create(
            body=b"raw file contents",
            asset_upload_metadata={},
        )
        assert_matches_type(AssetUploadCreateResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.asset_uploads.with_raw_response.create(
            body=b"raw file contents",
            asset_upload_metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset_upload = await response.parse()
        assert_matches_type(AssetUploadCreateResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.asset_uploads.with_streaming_response.create(
            body=b"raw file contents",
            asset_upload_metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset_upload = await response.parse()
            assert_matches_type(AssetUploadCreateResponse, asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        asset_upload = await async_client.asset_uploads.retrieve(
            "jobId",
        )
        assert_matches_type(AssetUploadRetrieveResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.asset_uploads.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset_upload = await response.parse()
        assert_matches_type(AssetUploadRetrieveResponse, asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.asset_uploads.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset_upload = await response.parse()
            assert_matches_type(AssetUploadRetrieveResponse, asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.asset_uploads.with_raw_response.retrieve(
                "",
            )
