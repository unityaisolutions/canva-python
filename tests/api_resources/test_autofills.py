# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import AutofillCreateResponse, AutofillRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutofills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        autofill = client.autofills.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {"cells": [{"type": "string"}, {"type": "string"}, {"type": "string"}, {"type": "string"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                        ]
                    },
                    "type": "chart",
                },
            },
        )
        assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Canva) -> None:
        autofill = client.autofills.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {
                                "cells": [
                                    {
                                        "type": "string",
                                        "value": "Geographic Region",
                                    },
                                    {
                                        "type": "string",
                                        "value": "Sales (millions AUD)",
                                    },
                                    {
                                        "type": "string",
                                        "value": "Target met?",
                                    },
                                    {
                                        "type": "string",
                                        "value": "Date met",
                                    },
                                ]
                            },
                            {
                                "cells": [
                                    {
                                        "type": "string",
                                        "value": "Asia Pacific",
                                    },
                                    {
                                        "type": "number",
                                        "value": 10.2,
                                    },
                                    {
                                        "type": "boolean",
                                        "value": True,
                                    },
                                    {
                                        "type": "date",
                                        "value": 1721944387,
                                    },
                                ]
                            },
                            {
                                "cells": [
                                    {
                                        "type": "string",
                                        "value": "EMEA",
                                    },
                                    {
                                        "type": "number",
                                        "value": 13.8,
                                    },
                                    {
                                        "type": "boolean",
                                        "value": False,
                                    },
                                    {
                                        "type": "date",
                                        "value": 0,
                                    },
                                ]
                            },
                        ]
                    },
                    "type": "chart",
                },
            },
            title="x",
        )
        assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.autofills.with_raw_response.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {"cells": [{"type": "string"}, {"type": "string"}, {"type": "string"}, {"type": "string"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                        ]
                    },
                    "type": "chart",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autofill = response.parse()
        assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.autofills.with_streaming_response.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {"cells": [{"type": "string"}, {"type": "string"}, {"type": "string"}, {"type": "string"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                        ]
                    },
                    "type": "chart",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autofill = response.parse()
            assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        autofill = client.autofills.retrieve(
            "jobId",
        )
        assert_matches_type(AutofillRetrieveResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.autofills.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autofill = response.parse()
        assert_matches_type(AutofillRetrieveResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.autofills.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autofill = response.parse()
            assert_matches_type(AutofillRetrieveResponse, autofill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.autofills.with_raw_response.retrieve(
                "",
            )


class TestAsyncAutofills:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        autofill = await async_client.autofills.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {"cells": [{"type": "string"}, {"type": "string"}, {"type": "string"}, {"type": "string"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                        ]
                    },
                    "type": "chart",
                },
            },
        )
        assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCanva) -> None:
        autofill = await async_client.autofills.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {
                                "cells": [
                                    {
                                        "type": "string",
                                        "value": "Geographic Region",
                                    },
                                    {
                                        "type": "string",
                                        "value": "Sales (millions AUD)",
                                    },
                                    {
                                        "type": "string",
                                        "value": "Target met?",
                                    },
                                    {
                                        "type": "string",
                                        "value": "Date met",
                                    },
                                ]
                            },
                            {
                                "cells": [
                                    {
                                        "type": "string",
                                        "value": "Asia Pacific",
                                    },
                                    {
                                        "type": "number",
                                        "value": 10.2,
                                    },
                                    {
                                        "type": "boolean",
                                        "value": True,
                                    },
                                    {
                                        "type": "date",
                                        "value": 1721944387,
                                    },
                                ]
                            },
                            {
                                "cells": [
                                    {
                                        "type": "string",
                                        "value": "EMEA",
                                    },
                                    {
                                        "type": "number",
                                        "value": 13.8,
                                    },
                                    {
                                        "type": "boolean",
                                        "value": False,
                                    },
                                    {
                                        "type": "date",
                                        "value": 0,
                                    },
                                ]
                            },
                        ]
                    },
                    "type": "chart",
                },
            },
            title="x",
        )
        assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.autofills.with_raw_response.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {"cells": [{"type": "string"}, {"type": "string"}, {"type": "string"}, {"type": "string"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                        ]
                    },
                    "type": "chart",
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autofill = await response.parse()
        assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.autofills.with_streaming_response.create(
            brand_template_id="DAFVztcvd9z",
            data={
                "cute_pet_image_of_the_day": {
                    "asset_id": "Msd59349ff",
                    "type": "image",
                },
                "cute_pet_witty_pet_says": {
                    "text": "It was like this when I got here!",
                    "type": "text",
                },
                "cute_pet_sales_chart": {
                    "chart_data": {
                        "rows": [
                            {"cells": [{"type": "string"}, {"type": "string"}, {"type": "string"}, {"type": "string"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                            {"cells": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}, {"type": "date"}]},
                        ]
                    },
                    "type": "chart",
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autofill = await response.parse()
            assert_matches_type(AutofillCreateResponse, autofill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        autofill = await async_client.autofills.retrieve(
            "jobId",
        )
        assert_matches_type(AutofillRetrieveResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.autofills.with_raw_response.retrieve(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autofill = await response.parse()
        assert_matches_type(AutofillRetrieveResponse, autofill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.autofills.with_streaming_response.retrieve(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autofill = await response.parse()
            assert_matches_type(AutofillRetrieveResponse, autofill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.autofills.with_raw_response.retrieve(
                "",
            )
