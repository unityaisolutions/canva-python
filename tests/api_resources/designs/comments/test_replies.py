# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from tests.utils import assert_matches_type
from canva.types.designs.comments import (
    ReplyListResponse,
    ReplyCreateResponse,
    ReplyRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReplies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        reply = client.designs.comments.replies.create(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            message_plaintext="Thanks!",
        )
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.designs.comments.replies.with_raw_response.create(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            message_plaintext="Thanks!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.designs.comments.replies.with_streaming_response.create(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            message_plaintext="Thanks!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyCreateResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.comments.replies.with_raw_response.create(
                thread_id="KeAbiEAjZEj",
                design_id="",
                message_plaintext="Thanks!",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.designs.comments.replies.with_raw_response.create(
                thread_id="",
                design_id="designId",
                message_plaintext="Thanks!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        reply = client.designs.comments.replies.retrieve(
            reply_id="KeAZEAjijEb",
            design_id="designId",
            thread_id="KeAbiEAjZEj",
        )
        assert_matches_type(ReplyRetrieveResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.designs.comments.replies.with_raw_response.retrieve(
            reply_id="KeAZEAjijEb",
            design_id="designId",
            thread_id="KeAbiEAjZEj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyRetrieveResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.designs.comments.replies.with_streaming_response.retrieve(
            reply_id="KeAZEAjijEb",
            design_id="designId",
            thread_id="KeAbiEAjZEj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyRetrieveResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.comments.replies.with_raw_response.retrieve(
                reply_id="KeAZEAjijEb",
                design_id="",
                thread_id="KeAbiEAjZEj",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.designs.comments.replies.with_raw_response.retrieve(
                reply_id="KeAZEAjijEb",
                design_id="designId",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reply_id` but received ''"):
            client.designs.comments.replies.with_raw_response.retrieve(
                reply_id="",
                design_id="designId",
                thread_id="KeAbiEAjZEj",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Canva) -> None:
        reply = client.designs.comments.replies.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )
        assert_matches_type(ReplyListResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Canva) -> None:
        reply = client.designs.comments.replies.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            continuation="continuation",
            limit=1,
        )
        assert_matches_type(ReplyListResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Canva) -> None:
        response = client.designs.comments.replies.with_raw_response.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = response.parse()
        assert_matches_type(ReplyListResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Canva) -> None:
        with client.designs.comments.replies.with_streaming_response.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = response.parse()
            assert_matches_type(ReplyListResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            client.designs.comments.replies.with_raw_response.list(
                thread_id="KeAbiEAjZEj",
                design_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.designs.comments.replies.with_raw_response.list(
                thread_id="",
                design_id="designId",
            )


class TestAsyncReplies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        reply = await async_client.designs.comments.replies.create(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            message_plaintext="Thanks!",
        )
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.comments.replies.with_raw_response.create(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            message_plaintext="Thanks!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyCreateResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.comments.replies.with_streaming_response.create(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            message_plaintext="Thanks!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyCreateResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.create(
                thread_id="KeAbiEAjZEj",
                design_id="",
                message_plaintext="Thanks!",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.create(
                thread_id="",
                design_id="designId",
                message_plaintext="Thanks!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        reply = await async_client.designs.comments.replies.retrieve(
            reply_id="KeAZEAjijEb",
            design_id="designId",
            thread_id="KeAbiEAjZEj",
        )
        assert_matches_type(ReplyRetrieveResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.comments.replies.with_raw_response.retrieve(
            reply_id="KeAZEAjijEb",
            design_id="designId",
            thread_id="KeAbiEAjZEj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyRetrieveResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.comments.replies.with_streaming_response.retrieve(
            reply_id="KeAZEAjijEb",
            design_id="designId",
            thread_id="KeAbiEAjZEj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyRetrieveResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.retrieve(
                reply_id="KeAZEAjijEb",
                design_id="",
                thread_id="KeAbiEAjZEj",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.retrieve(
                reply_id="KeAZEAjijEb",
                design_id="designId",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reply_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.retrieve(
                reply_id="",
                design_id="designId",
                thread_id="KeAbiEAjZEj",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCanva) -> None:
        reply = await async_client.designs.comments.replies.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )
        assert_matches_type(ReplyListResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCanva) -> None:
        reply = await async_client.designs.comments.replies.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
            continuation="continuation",
            limit=1,
        )
        assert_matches_type(ReplyListResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCanva) -> None:
        response = await async_client.designs.comments.replies.with_raw_response.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reply = await response.parse()
        assert_matches_type(ReplyListResponse, reply, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCanva) -> None:
        async with async_client.designs.comments.replies.with_streaming_response.list(
            thread_id="KeAbiEAjZEj",
            design_id="designId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reply = await response.parse()
            assert_matches_type(ReplyListResponse, reply, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `design_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.list(
                thread_id="KeAbiEAjZEj",
                design_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.designs.comments.replies.with_raw_response.list(
                thread_id="",
                design_id="designId",
            )
