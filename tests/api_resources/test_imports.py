# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import ImportCreateResponse, ImportRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        import_ = client.imports.create(
            body=b"raw file contents",
            import_metadata={},
        )
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.imports.with_raw_response.create(
            body=b"raw file contents",
            import_metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.imports.with_streaming_response.create(
            body=b"raw file contents",
            import_metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(ImportCreateResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        import_ = client.imports.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )
        assert_matches_type(ImportRetrieveResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.imports.with_raw_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(ImportRetrieveResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.imports.with_streaming_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(ImportRetrieveResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.imports.with_raw_response.retrieve(
                "",
            )


class TestAsyncImports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        import_ = await async_client.imports.create(
            body=b"raw file contents",
            import_metadata={},
        )
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.imports.with_raw_response.create(
            body=b"raw file contents",
            import_metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.imports.with_streaming_response.create(
            body=b"raw file contents",
            import_metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(ImportCreateResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        import_ = await async_client.imports.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )
        assert_matches_type(ImportRetrieveResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.imports.with_raw_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(ImportRetrieveResponse, import_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.imports.with_streaming_response.retrieve(
            "f81b26fd-a33d-4c2d-9e8c-4a7aca798b17",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(ImportRetrieveResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.imports.with_raw_response.retrieve(
                "",
            )
