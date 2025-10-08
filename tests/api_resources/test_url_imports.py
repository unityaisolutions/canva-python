# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import URLImportCreateResponse, URLImportRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLImports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        url_import = client.url_imports.create(
            title="My Awesome Design",
            url="x",
        )
        assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Canva) -> None:
        url_import = client.url_imports.create(
            title="My Awesome Design",
            url="x",
            mime_type="application/vnd.apple.keynote",
        )
        assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.url_imports.with_raw_response.create(
            title="My Awesome Design",
            url="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_import = response.parse()
        assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.url_imports.with_streaming_response.create(
            title="My Awesome Design",
            url="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_import = response.parse()
            assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        url_import = client.url_imports.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )
        assert_matches_type(URLImportRetrieveResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.url_imports.with_raw_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_import = response.parse()
        assert_matches_type(URLImportRetrieveResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.url_imports.with_streaming_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_import = response.parse()
            assert_matches_type(URLImportRetrieveResponse, url_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.url_imports.with_raw_response.retrieve(
                "",
            )


class TestAsyncURLImports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        url_import = await async_client.url_imports.create(
            title="My Awesome Design",
            url="x",
        )
        assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCanva) -> None:
        url_import = await async_client.url_imports.create(
            title="My Awesome Design",
            url="x",
            mime_type="application/vnd.apple.keynote",
        )
        assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.url_imports.with_raw_response.create(
            title="My Awesome Design",
            url="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_import = await response.parse()
        assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.url_imports.with_streaming_response.create(
            title="My Awesome Design",
            url="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_import = await response.parse()
            assert_matches_type(URLImportCreateResponse, url_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        url_import = await async_client.url_imports.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )
        assert_matches_type(URLImportRetrieveResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.url_imports.with_raw_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_import = await response.parse()
        assert_matches_type(URLImportRetrieveResponse, url_import, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.url_imports.with_streaming_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_import = await response.parse()
            assert_matches_type(URLImportRetrieveResponse, url_import, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.url_imports.with_raw_response.retrieve(
                "",
            )
