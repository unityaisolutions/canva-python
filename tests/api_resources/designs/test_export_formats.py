# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from tests.utils import assert_matches_type
from canva.types.designs import ExportFormatRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExportFormats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        export_format = client.designs.export_formats.retrieve(
            "designId",
        )
        assert_matches_type(ExportFormatRetrieveResponse, export_format, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.designs.export_formats.with_raw_response.retrieve(
            "designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_format = response.parse()
        assert_matches_type(ExportFormatRetrieveResponse, export_format, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.designs.export_formats.with_streaming_response.retrieve(
            "designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_format = response.parse()
            assert_matches_type(ExportFormatRetrieveResponse, export_format, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.export_formats.with_raw_response.retrieve(
                "",
            )


class TestAsyncExportFormats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        export_format = await async_client.designs.export_formats.retrieve(
            "designId",
        )
        assert_matches_type(ExportFormatRetrieveResponse, export_format, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.export_formats.with_raw_response.retrieve(
            "designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_format = await response.parse()
        assert_matches_type(ExportFormatRetrieveResponse, export_format, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.export_formats.with_streaming_response.retrieve(
            "designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_format = await response.parse()
            assert_matches_type(ExportFormatRetrieveResponse, export_format, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.export_formats.with_raw_response.retrieve(
                "",
            )
