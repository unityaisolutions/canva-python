# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .asset import Asset
from .._models import BaseModel

__all__ = ["AssetUpdateResponse"]


class AssetUpdateResponse(BaseModel):
    asset: Asset
    """The asset object, which contains metadata about the asset."""
