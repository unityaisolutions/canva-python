# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .folder import Folder
from .._utils import PropertyInfo
from .._models import BaseModel
from .thumbnail import Thumbnail
from .asset_type import AssetType
from .design_summary import DesignSummary

__all__ = ["FolderListItemsResponse", "Item", "ItemFolderItem", "ItemDesignItem", "ItemImageItem", "ItemImageItemImage"]


class ItemFolderItem(BaseModel):
    folder: Folder
    """The folder object, which contains metadata about the folder."""

    type: Literal["folder"]


class ItemDesignItem(BaseModel):
    design: DesignSummary
    """Basic details about the design, such as the design's ID, title, and URL."""

    type: Literal["design"]


class ItemImageItemImage(BaseModel):
    id: str
    """The ID of the asset."""

    created_at: int
    """
    When the asset was added to Canva, as a Unix timestamp (in seconds since the
    Unix Epoch).
    """

    name: str
    """The name of the asset."""

    tags: List[str]
    """
    The user-facing tags attached to the asset. Users can add these tags to their
    uploaded assets, and they can search their uploaded assets in the Canva UI by
    searching for these tags. For information on how users use tags, see the
    [Canva Help Center page on asset tags](https://www.canva.com/help/add-edit-tags/).
    """

    type: AssetType
    """Type of an asset."""

    updated_at: int
    """
    When the asset was last updated in Canva, as a Unix timestamp (in seconds since
    the Unix Epoch).
    """

    thumbnail: Optional[Thumbnail] = None
    """A thumbnail image representing the object."""


class ItemImageItem(BaseModel):
    image: ItemImageItemImage
    """An object representing an asset with associated metadata."""

    type: Literal["image"]


Item: TypeAlias = Annotated[Union[ItemFolderItem, ItemDesignItem, ItemImageItem], PropertyInfo(discriminator="type")]


class FolderListItemsResponse(BaseModel):
    items: List[Item]
    """An array of items in the folder."""

    continuation: Optional[str] = None
    """
    If the success response contains a continuation token, the folder contains more
    items you can list. You can use this token as a query parameter and retrieve
    more items from the list, for example
    `/v1/folders/{folderId}/items?continuation={continuation}`.

    To retrieve all the items in a folder, you might need to make multiple requests.
    """
