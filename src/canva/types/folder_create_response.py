# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .folder import Folder
from .._models import BaseModel

__all__ = ["FolderCreateResponse"]


class FolderCreateResponse(BaseModel):
    folder: Optional[Folder] = None
    """The folder object, which contains metadata about the folder."""
