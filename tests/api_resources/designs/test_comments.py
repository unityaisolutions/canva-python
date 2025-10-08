# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from tests.utils import assert_matches_type
from canva.types.designs import CommentCreateResponse, CommentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        comment = client.designs.comments.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Canva) -> None:
        comment = client.designs.comments.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            assignee_id="oUnPjZ2k2yuhftbWF7873o",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.designs.comments.with_raw_response.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.designs.comments.with_streaming_response.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.comments.with_raw_response.create(
                design_id="",
                message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        comment = client.designs.comments.retrieve(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.designs.comments.with_raw_response.retrieve(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.designs.comments.with_streaming_response.retrieve(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.comments.with_raw_response.retrieve(
                thread_id="KeAbiEAjZEj",
                design_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.designs.comments.with_raw_response.retrieve(
                thread_id="",
                design_id="designId",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        comment = await async_client.designs.comments.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCanva) -> None:
        comment = await async_client.designs.comments.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            assignee_id="oUnPjZ2k2yuhftbWF7873o",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.comments.with_raw_response.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.comments.with_streaming_response.create(
            design_id="designId",
            message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.comments.with_raw_response.create(
                design_id="",
                message_plaintext="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        comment = await async_client.designs.comments.retrieve(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.comments.with_raw_response.retrieve(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.comments.with_streaming_response.retrieve(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentRetrieveResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.comments.with_raw_response.retrieve(
                thread_id="KeAbiEAjZEj",
                design_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.designs.comments.with_raw_response.retrieve(
                thread_id="",
                design_id="designId",
            )
