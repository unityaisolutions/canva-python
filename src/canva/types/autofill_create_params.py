# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AutofillCreateParams",
    "Data",
    "DataDatasetImageValue",
    "DataDatasetTextValue",
    "DataDatasetChartValue",
    "DataDatasetChartValueChartData",
    "DataDatasetChartValueChartDataRow",
    "DataDatasetChartValueChartDataRowCell",
    "DataDatasetChartValueChartDataRowCellStringDataTableCell",
    "DataDatasetChartValueChartDataRowCellNumberDataTableCell",
    "DataDatasetChartValueChartDataRowCellBooleanDataTableCell",
    "DataDatasetChartValueChartDataRowCellDateDataTableCell",
]


class AutofillCreateParams(TypedDict, total=False):
    brand_template_id: Required[str]
    """ID of the input brand template."""

    data: Required[Dict[str, Data]]
    """Data object containing the data fields and values to autofill."""

    title: str
    """Title to use for the autofilled design.

    If no design title is provided, the autofilled design will have the same title
    as the brand template.
    """


class DataDatasetImageValue(TypedDict, total=False):
    asset_id: Required[str]
    """`asset_id` of the image to insert into the template element."""

    type: Required[Literal["image"]]


class DataDatasetTextValue(TypedDict, total=False):
    text: Required[str]
    """Text to insert into the template element."""

    type: Required[Literal["text"]]


class DataDatasetChartValueChartDataRowCellStringDataTableCell(TypedDict, total=False):
    type: Required[Literal["string"]]

    value: str


class DataDatasetChartValueChartDataRowCellNumberDataTableCell(TypedDict, total=False):
    type: Required[Literal["number"]]

    value: float


class DataDatasetChartValueChartDataRowCellBooleanDataTableCell(TypedDict, total=False):
    type: Required[Literal["boolean"]]

    value: bool


class DataDatasetChartValueChartDataRowCellDateDataTableCell(TypedDict, total=False):
    type: Required[Literal["date"]]

    value: int


DataDatasetChartValueChartDataRowCell: TypeAlias = Union[
    DataDatasetChartValueChartDataRowCellStringDataTableCell,
    DataDatasetChartValueChartDataRowCellNumberDataTableCell,
    DataDatasetChartValueChartDataRowCellBooleanDataTableCell,
    DataDatasetChartValueChartDataRowCellDateDataTableCell,
]


class DataDatasetChartValueChartDataRow(TypedDict, total=False):
    cells: Required[Iterable[DataDatasetChartValueChartDataRowCell]]
    """Cells of data in row.

    All rows must have the same number of cells.
    """


class DataDatasetChartValueChartData(TypedDict, total=False):
    rows: Required[Iterable[DataDatasetChartValueChartDataRow]]
    """Rows of data.

    The first row usually contains column headers.
    """


class DataDatasetChartValue(TypedDict, total=False):
    chart_data: Required[DataDatasetChartValueChartData]
    """Tabular data, structured in rows of cells.

    - The first row usually contains column headers.
    - Each cell must have a data type configured.
    - All rows must have the same number of cells.
    - Maximum of 100 rows and 20 columns.

    WARNING: Chart data fields are a
    [preview feature](https://www.canva.dev/docs/connect/#preview-apis). There might
    be unannounced breaking changes to this feature which won't produce a new API
    version.
    """

    type: Required[Literal["chart"]]


Data: TypeAlias = Union[DataDatasetImageValue, DataDatasetTextValue, DataDatasetChartValue]
