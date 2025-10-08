# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DesignLinks"]


class DesignLinks(BaseModel):
    edit_url: str
    """A temporary editing URL for the design.

    This URL is only accessible to the user that made the API request, and is
    designed to support
    [return navigation](https://www.canva.dev/docs/connect/return-navigation-guide/)
    workflows.

    NOTE: This is not a permanent URL, it is only valid for 30 days.
    """

    view_url: str
    """A temporary viewing URL for the design.

    This URL is only accessible to the user that made the API request, and is
    designed to support
    [return navigation](https://www.canva.dev/docs/connect/return-navigation-guide/)
    workflows.

    NOTE: This is not a permanent URL, it is only valid for 30 days.
    """
