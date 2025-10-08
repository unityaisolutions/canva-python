# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import folder_create_params, folder_update_params, folder_move_item_params, folder_list_items_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.folder_create_response import FolderCreateResponse
from ..types.folder_update_response import FolderUpdateResponse
from ..types.folder_retrieve_response import FolderRetrieveResponse
from ..types.folder_list_items_response import FolderListItemsResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parent_folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Creates a folder in one of the following locations:

        - The top level of a Canva user's
          [projects](https://www.canva.com/help/find-designs-and-folders/) (using the ID
          `root`),
        - The user's Uploads folder (using the ID `uploads`),
        - Another folder (using the parent folder's ID).

        When a folder is successfully created, the endpoint returns its folder ID, along
        with other information.

        Args:
          name: The name of the folder.

          parent_folder_id: The folder ID of the parent folder. To create a new folder at the top level of a
              user's [projects](https://www.canva.com/help/find-designs-and-folders/), use the
              ID `root`. To create it in their Uploads folder, use `uploads`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/folders",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    def retrieve(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderRetrieveResponse:
        """
        Gets the name and other details of a folder using a folder's `folderID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderRetrieveResponse,
        )

    def update(
        self,
        folder_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """Updates a folder's details using its `folderID`.

        Currently, you can only update
        a folder's name.

        Args:
          name: The folder name, as shown in the Canva UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._patch(
            f"/v1/folders/{folder_id}",
            body=maybe_transform({"name": name}, folder_update_params.FolderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a folder with the specified `folderID`.

        Deleting a folder moves the
        user's content in the folder to the
        [Trash](https://www.canva.com/help/deleted-designs/) and content owned by other
        users is moved to the top level of the owner's
        [projects](https://www.canva.com/help/find-designs-and-folders/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_items(
        self,
        folder_id: str,
        *,
        continuation: str | Omit = omit,
        item_types: List[Literal["design", "folder", "image"]] | Omit = omit,
        sort_by: Literal[
            "created_ascending",
            "created_descending",
            "modified_ascending",
            "modified_descending",
            "title_ascending",
            "title_descending",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListItemsResponse:
        """
        Lists the items in a folder, including each item's `type`.

        Folders can contain:

        - Other folders.
        - Designs, such as Instagram posts, Presentations, and Documents
          ([Canva Docs](https://www.canva.com/create/documents/)).
        - Image assets.

        Currently, video assets are not returned in the response.

        Args:
          continuation: If the success response contains a continuation token, the folder contains more
              items you can list. You can use this token as a query parameter and retrieve
              more items from the list, for example
              `/v1/folders/{folderId}/items?continuation={continuation}`.

              To retrieve all the items in a folder, you might need to make multiple requests.

          item_types:
              Filter the folder items to only return specified types. The available types are:
              `design`, `folder`, and `image`. To filter for more than one item type, provide
              a comma- delimited list.

          sort_by: Sort the list of folder items.

              - `created_ascending` - Sort results by creation date, in ascending order.
              - `created_descending` - Sort results by creation date, in descending order.
              - `modified_ascending` - Sort results by the last modified date, in ascending
                order.
              - `modified_descending` - Sort results by the last modified date, in descending
                order.
              - `title_ascending` - Sort results by title, in ascending order. The title is
                either the `name` field for a folder or asset, or the `title` field for a
                design.
              - `title_descending` - Sort results by title, in descending order. The title is
                either the `name` field for a folder or asset, or the `title` field for a
                design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/v1/folders/{folder_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "continuation": continuation,
                        "item_types": item_types,
                        "sort_by": sort_by,
                    },
                    folder_list_items_params.FolderListItemsParams,
                ),
            ),
            cast_to=FolderListItemsResponse,
        )

    def move_item(
        self,
        *,
        item_id: str,
        to_folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Moves an item to another folder.

        You must specify the folder ID of the
        destination folder, as well as the ID of the item you want to move.

        NOTE: In some situations, a single item can exist in multiple folders. If you
        attempt to move an item that exists in multiple folders, the API returns an
        `item_in_multiple_folders` error. In this case, you must use the Canva UI to
        move the item to another folder.

        Args:
          item_id: The ID of the item you want to move. Currently, video assets are not supported.

          to_folder_id: The ID of the folder you want to move the item to (the destination folder). If
              you want to move the item to the top level of a Canva user's
              [projects](https://www.canva.com/help/find-designs-and-folders/), use the ID
              `root`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/folders/move",
            body=maybe_transform(
                {
                    "item_id": item_id,
                    "to_folder_id": to_folder_id,
                },
                folder_move_item_params.FolderMoveItemParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unityaisolutions/canva-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unityaisolutions/canva-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parent_folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """
        Creates a folder in one of the following locations:

        - The top level of a Canva user's
          [projects](https://www.canva.com/help/find-designs-and-folders/) (using the ID
          `root`),
        - The user's Uploads folder (using the ID `uploads`),
        - Another folder (using the parent folder's ID).

        When a folder is successfully created, the endpoint returns its folder ID, along
        with other information.

        Args:
          name: The name of the folder.

          parent_folder_id: The folder ID of the parent folder. To create a new folder at the top level of a
              user's [projects](https://www.canva.com/help/find-designs-and-folders/), use the
              ID `root`. To create it in their Uploads folder, use `uploads`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/folders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    async def retrieve(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderRetrieveResponse:
        """
        Gets the name and other details of a folder using a folder's `folderID`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderRetrieveResponse,
        )

    async def update(
        self,
        folder_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """Updates a folder's details using its `folderID`.

        Currently, you can only update
        a folder's name.

        Args:
          name: The folder name, as shown in the Canva UI.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._patch(
            f"/v1/folders/{folder_id}",
            body=await async_maybe_transform({"name": name}, folder_update_params.FolderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a folder with the specified `folderID`.

        Deleting a folder moves the
        user's content in the folder to the
        [Trash](https://www.canva.com/help/deleted-designs/) and content owned by other
        users is moved to the top level of the owner's
        [projects](https://www.canva.com/help/find-designs-and-folders/).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_items(
        self,
        folder_id: str,
        *,
        continuation: str | Omit = omit,
        item_types: List[Literal["design", "folder", "image"]] | Omit = omit,
        sort_by: Literal[
            "created_ascending",
            "created_descending",
            "modified_ascending",
            "modified_descending",
            "title_ascending",
            "title_descending",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderListItemsResponse:
        """
        Lists the items in a folder, including each item's `type`.

        Folders can contain:

        - Other folders.
        - Designs, such as Instagram posts, Presentations, and Documents
          ([Canva Docs](https://www.canva.com/create/documents/)).
        - Image assets.

        Currently, video assets are not returned in the response.

        Args:
          continuation: If the success response contains a continuation token, the folder contains more
              items you can list. You can use this token as a query parameter and retrieve
              more items from the list, for example
              `/v1/folders/{folderId}/items?continuation={continuation}`.

              To retrieve all the items in a folder, you might need to make multiple requests.

          item_types:
              Filter the folder items to only return specified types. The available types are:
              `design`, `folder`, and `image`. To filter for more than one item type, provide
              a comma- delimited list.

          sort_by: Sort the list of folder items.

              - `created_ascending` - Sort results by creation date, in ascending order.
              - `created_descending` - Sort results by creation date, in descending order.
              - `modified_ascending` - Sort results by the last modified date, in ascending
                order.
              - `modified_descending` - Sort results by the last modified date, in descending
                order.
              - `title_ascending` - Sort results by title, in ascending order. The title is
                either the `name` field for a folder or asset, or the `title` field for a
                design.
              - `title_descending` - Sort results by title, in descending order. The title is
                either the `name` field for a folder or asset, or the `title` field for a
                design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/v1/folders/{folder_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "continuation": continuation,
                        "item_types": item_types,
                        "sort_by": sort_by,
                    },
                    folder_list_items_params.FolderListItemsParams,
                ),
            ),
            cast_to=FolderListItemsResponse,
        )

    async def move_item(
        self,
        *,
        item_id: str,
        to_folder_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Moves an item to another folder.

        You must specify the folder ID of the
        destination folder, as well as the ID of the item you want to move.

        NOTE: In some situations, a single item can exist in multiple folders. If you
        attempt to move an item that exists in multiple folders, the API returns an
        `item_in_multiple_folders` error. In this case, you must use the Canva UI to
        move the item to another folder.

        Args:
          item_id: The ID of the item you want to move. Currently, video assets are not supported.

          to_folder_id: The ID of the folder you want to move the item to (the destination folder). If
              you want to move the item to the top level of a Canva user's
              [projects](https://www.canva.com/help/find-designs-and-folders/), use the ID
              `root`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/folders/move",
            body=await async_maybe_transform(
                {
                    "item_id": item_id,
                    "to_folder_id": to_folder_id,
                },
                folder_move_item_params.FolderMoveItemParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            folders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            folders.update,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.list_items = to_raw_response_wrapper(
            folders.list_items,
        )
        self.move_item = to_raw_response_wrapper(
            folders.move_item,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            folders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            folders.update,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.list_items = async_to_raw_response_wrapper(
            folders.list_items,
        )
        self.move_item = async_to_raw_response_wrapper(
            folders.move_item,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            folders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.list_items = to_streamed_response_wrapper(
            folders.list_items,
        )
        self.move_item = to_streamed_response_wrapper(
            folders.move_item,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            folders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.list_items = async_to_streamed_response_wrapper(
            folders.list_items,
        )
        self.move_item = async_to_streamed_response_wrapper(
            folders.move_item,
        )
