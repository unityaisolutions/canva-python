# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import (
    CommentCreateReplyResponse,
    CommentCreateThreadResponse,
)
from tests.utils import assert_matches_type

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_reply(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            comment = client.comments.create_reply(
                comment_id="KeAZEAjijEb",
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Thanks!",
            )

        assert_matches_type(CommentCreateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_reply(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.comments.with_raw_response.create_reply(
                comment_id="KeAZEAjijEb",
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Thanks!",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_reply(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            with client.comments.with_streaming_response.create_reply(
                comment_id="KeAZEAjijEb",
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Thanks!",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                comment = response.parse()
                assert_matches_type(CommentCreateReplyResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_reply(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
                client.comments.with_raw_response.create_reply(
                    comment_id="",
                    attached_to={
                        "design_id": "DAFVztcvd9z",
                        "type": "design",
                    },
                    message="Thanks!",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_thread(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            comment = client.comments.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            )

        assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_thread_with_all_params(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            comment = client.comments.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
                assignee_id="oUnPjZ2k2yuhftbWF7873o",
            )

        assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_thread(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.comments.with_raw_response.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_thread(self, client: Canva) -> None:
        with pytest.warns(DeprecationWarning):
            with client.comments.with_streaming_response.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                comment = response.parse()
                assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_reply(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            comment = await async_client.comments.create_reply(
                comment_id="KeAZEAjijEb",
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Thanks!",
            )

        assert_matches_type(CommentCreateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_reply(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.comments.with_raw_response.create_reply(
                comment_id="KeAZEAjijEb",
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Thanks!",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateReplyResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_reply(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.comments.with_streaming_response.create_reply(
                comment_id="KeAZEAjijEb",
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Thanks!",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                comment = await response.parse()
                assert_matches_type(CommentCreateReplyResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_reply(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_id` but received ''"):
                await async_client.comments.with_raw_response.create_reply(
                    comment_id="",
                    attached_to={
                        "design_id": "DAFVztcvd9z",
                        "type": "design",
                    },
                    message="Thanks!",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_thread(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            comment = await async_client.comments.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            )

        assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_thread_with_all_params(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            comment = await async_client.comments.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
                assignee_id="oUnPjZ2k2yuhftbWF7873o",
            )

        assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_thread(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.comments.with_raw_response.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_thread(self, async_client: AsyncCanva) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.comments.with_streaming_response.create_thread(
                attached_to={
                    "design_id": "DAFVztcvd9z",
                    "type": "design",
                },
                message="Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                comment = await response.parse()
                assert_matches_type(CommentCreateThreadResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True
