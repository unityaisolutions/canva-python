# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "BrandTemplateRetrieveDatasetResponse",
    "Dataset",
    "DatasetImageDataField",
    "DatasetTextDataField",
    "DatasetChartDataField",
]


class DatasetImageDataField(BaseModel):
    type: Literal["image"]


class DatasetTextDataField(BaseModel):
    type: Literal["text"]


class DatasetChartDataField(BaseModel):
    type: Literal["chart"]


Dataset: TypeAlias = Annotated[
    Union[DatasetImageDataField, DatasetTextDataField, DatasetChartDataField], PropertyInfo(discriminator="type")
]


class BrandTemplateRetrieveDatasetResponse(BaseModel):
    dataset: Optional[Dict[str, Dataset]] = None
    """The dataset definition for the brand template.

    The dataset definition contains the data inputs available for use with the
    [Create design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/create-design-autofill-job/).
    """
