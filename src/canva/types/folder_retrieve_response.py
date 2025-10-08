# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .folder import Folder
from .._models import BaseModel

__all__ = ["FolderRetrieveResponse"]


class FolderRetrieveResponse(BaseModel):
    folder: Folder
    """The folder object, which contains metadata about the folder."""
