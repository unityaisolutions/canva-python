# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .asset_upload_job import AssetUploadJob

__all__ = ["URLAssetUploadCreateResponse"]


class URLAssetUploadCreateResponse(BaseModel):
    job: AssetUploadJob
    """The status of the asset upload job."""
