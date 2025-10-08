# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import (
    FolderCreateResponse,
    FolderUpdateResponse,
    FolderRetrieveResponse,
    FolderListItemsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Canva) -> None:
        folder = client.folders.create(
            name="My awesome holiday",
            parent_folder_id="FAF2lZtloor",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Canva) -> None:
        response = client.folders.with_raw_response.create(
            name="My awesome holiday",
            parent_folder_id="FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Canva) -> None:
        with client.folders.with_streaming_response.create(
            name="My awesome holiday",
            parent_folder_id="FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Canva) -> None:
        folder = client.folders.retrieve(
            "FAF2lZtloor",
        )
        assert_matches_type(FolderRetrieveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Canva) -> None:
        response = client.folders.with_raw_response.retrieve(
            "FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderRetrieveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Canva) -> None:
        with client.folders.with_streaming_response.retrieve(
            "FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderRetrieveResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Canva) -> None:
        folder = client.folders.update(
            folder_id="FAF2lZtloor",
            name="My awesome holiday",
        )
        assert_matches_type(FolderUpdateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Canva) -> None:
        response = client.folders.with_raw_response.update(
            folder_id="FAF2lZtloor",
            name="My awesome holiday",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderUpdateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Canva) -> None:
        with client.folders.with_streaming_response.update(
            folder_id="FAF2lZtloor",
            name="My awesome holiday",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderUpdateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.update(
                folder_id="",
                name="My awesome holiday",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Canva) -> None:
        folder = client.folders.delete(
            "FAF2lZtloor",
        )
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Canva) -> None:
        response = client.folders.with_raw_response.delete(
            "FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Canva) -> None:
        with client.folders.with_streaming_response.delete(
            "FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_items(self, client: Canva) -> None:
        folder = client.folders.list_items(
            folder_id="FAF2lZtloor",
        )
        assert_matches_type(FolderListItemsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_items_with_all_params(self, client: Canva) -> None:
        folder = client.folders.list_items(
            folder_id="FAF2lZtloor",
            continuation="continuation",
            item_types=["design"],
            sort_by="created_ascending",
        )
        assert_matches_type(FolderListItemsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_items(self, client: Canva) -> None:
        response = client.folders.with_raw_response.list_items(
            folder_id="FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderListItemsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_items(self, client: Canva) -> None:
        with client.folders.with_streaming_response.list_items(
            folder_id="FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderListItemsResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_items(self, client: Canva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.folders.with_raw_response.list_items(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move_item(self, client: Canva) -> None:
        folder = client.folders.move_item(
            item_id="Msd59349ff",
            to_folder_id="FAF2lZtloor",
        )
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_move_item(self, client: Canva) -> None:
        response = client.folders.with_raw_response.move_item(
            item_id="Msd59349ff",
            to_folder_id="FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_move_item(self, client: Canva) -> None:
        with client.folders.with_streaming_response.move_item(
            item_id="Msd59349ff",
            to_folder_id="FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.create(
            name="My awesome holiday",
            parent_folder_id="FAF2lZtloor",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCanva) -> None:
        response = await async_client.folders.with_raw_response.create(
            name="My awesome holiday",
            parent_folder_id="FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCanva) -> None:
        async with async_client.folders.with_streaming_response.create(
            name="My awesome holiday",
            parent_folder_id="FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.retrieve(
            "FAF2lZtloor",
        )
        assert_matches_type(FolderRetrieveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCanva) -> None:
        response = await async_client.folders.with_raw_response.retrieve(
            "FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderRetrieveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCanva) -> None:
        async with async_client.folders.with_streaming_response.retrieve(
            "FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderRetrieveResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.update(
            folder_id="FAF2lZtloor",
            name="My awesome holiday",
        )
        assert_matches_type(FolderUpdateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCanva) -> None:
        response = await async_client.folders.with_raw_response.update(
            folder_id="FAF2lZtloor",
            name="My awesome holiday",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderUpdateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCanva) -> None:
        async with async_client.folders.with_streaming_response.update(
            folder_id="FAF2lZtloor",
            name="My awesome holiday",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderUpdateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.update(
                folder_id="",
                name="My awesome holiday",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.delete(
            "FAF2lZtloor",
        )
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCanva) -> None:
        response = await async_client.folders.with_raw_response.delete(
            "FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCanva) -> None:
        async with async_client.folders.with_streaming_response.delete(
            "FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_items(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.list_items(
            folder_id="FAF2lZtloor",
        )
        assert_matches_type(FolderListItemsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_items_with_all_params(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.list_items(
            folder_id="FAF2lZtloor",
            continuation="continuation",
            item_types=["design"],
            sort_by="created_ascending",
        )
        assert_matches_type(FolderListItemsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_items(self, async_client: AsyncCanva) -> None:
        response = await async_client.folders.with_raw_response.list_items(
            folder_id="FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderListItemsResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_items(self, async_client: AsyncCanva) -> None:
        async with async_client.folders.with_streaming_response.list_items(
            folder_id="FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderListItemsResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_items(self, async_client: AsyncCanva) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.folders.with_raw_response.list_items(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move_item(self, async_client: AsyncCanva) -> None:
        folder = await async_client.folders.move_item(
            item_id="Msd59349ff",
            to_folder_id="FAF2lZtloor",
        )
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_move_item(self, async_client: AsyncCanva) -> None:
        response = await async_client.folders.with_raw_response.move_item(
            item_id="Msd59349ff",
            to_folder_id="FAF2lZtloor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert folder is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_move_item(self, async_client: AsyncCanva) -> None:
        async with async_client.folders.with_streaming_response.move_item(
            item_id="Msd59349ff",
            to_folder_id="FAF2lZtloor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert folder is None

        assert cast(Any, response.is_closed) is True
