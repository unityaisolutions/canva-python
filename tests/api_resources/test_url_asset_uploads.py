# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import URLAssetUploadCreateResponse, URLAssetUploadRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLAssetUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        url_asset_upload = client.url_asset_uploads.create(
            name="My Awesome Asset",
            url="https://example.com/my_asset_to_upload.jpg",
        )
        assert_matches_type(URLAssetUploadCreateResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.url_asset_uploads.with_raw_response.create(
            name="My Awesome Asset",
            url="https://example.com/my_asset_to_upload.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_asset_upload = response.parse()
        assert_matches_type(URLAssetUploadCreateResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.url_asset_uploads.with_streaming_response.create(
            name="My Awesome Asset",
            url="https://example.com/my_asset_to_upload.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_asset_upload = response.parse()
            assert_matches_type(URLAssetUploadCreateResponse, url_asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        url_asset_upload = client.url_asset_uploads.retrieve(
            "jobId",
        )
        assert_matches_type(URLAssetUploadRetrieveResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.url_asset_uploads.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_asset_upload = response.parse()
        assert_matches_type(URLAssetUploadRetrieveResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.url_asset_uploads.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_asset_upload = response.parse()
            assert_matches_type(URLAssetUploadRetrieveResponse, url_asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.url_asset_uploads.with_raw_response.retrieve(
                "",
            )


class TestAsyncURLAssetUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        url_asset_upload = await async_client.url_asset_uploads.create(
            name="My Awesome Asset",
            url="https://example.com/my_asset_to_upload.jpg",
        )
        assert_matches_type(URLAssetUploadCreateResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.url_asset_uploads.with_raw_response.create(
            name="My Awesome Asset",
            url="https://example.com/my_asset_to_upload.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_asset_upload = await response.parse()
        assert_matches_type(URLAssetUploadCreateResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.url_asset_uploads.with_streaming_response.create(
            name="My Awesome Asset",
            url="https://example.com/my_asset_to_upload.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_asset_upload = await response.parse()
            assert_matches_type(URLAssetUploadCreateResponse, url_asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        url_asset_upload = await async_client.url_asset_uploads.retrieve(
            "jobId",
        )
        assert_matches_type(URLAssetUploadRetrieveResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.url_asset_uploads.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_asset_upload = await response.parse()
        assert_matches_type(URLAssetUploadRetrieveResponse, url_asset_upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.url_asset_uploads.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_asset_upload = await response.parse()
            assert_matches_type(URLAssetUploadRetrieveResponse, url_asset_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.url_asset_uploads.with_raw_response.retrieve(
                "",
            )
