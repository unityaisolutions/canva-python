# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExportJob", "Error"]


class Error(BaseModel):
    code: Literal["license_required", "approval_required", "internal_failure"]
    """If the export failed, this specifies the reason why it failed.

    - `license_required`: The design contains
      [premium elements](https://www.canva.com/help/premium-elements/) that haven't
      been purchased. You can either buy the elements or upgrade to a Canva plan
      (such as Canva Pro) that has premium features, then try again. Alternatively,
      you can set `export_quality` to `regular` to export your document in regular
      quality.
    - `approval_required`: The design requires
      [reviewer approval](https://www.canva.com/en_au/help/design-approval/) before
      it can be exported.
    - `internal_failure`: The service encountered an error when exporting your
      design.

    - `license_required` - The design contains
      [premium elements](https://www.canva.com/help/premium-elements/) that haven't
      been purchased. You can either buy the elements or upgrade to a Canva plan
      (such as Canva Pro) that has premium features, then try again. Alternatively,
      you can set `export_quality` to `regular` to export your document in regular
      quality.
    - `approval_required` - The design requires
      [reviewer approval](https://www.canva.com/en_au/help/design-approval/) before
      it can be exported.
    - `internal_failure` - The service encountered an error when exporting your
      design.
    """

    message: str
    """A human-readable description of what went wrong."""


class ExportJob(BaseModel):
    id: str
    """The export job ID."""

    status: Literal["failed", "in_progress", "success"]
    """The export status of the job.

    A newly created job will be `in_progress` and will eventually become `success`
    or `failed`.
    """

    error: Optional[Error] = None
    """If the export fails, this object provides details about the error."""

    urls: Optional[List[str]] = None
    """Download URL(s) for the completed export job. These URLs expire after 24 hours.

    Depending on the design type and export format, there is a download URL for each
    page in the design. The list is sorted by page order.
    """
