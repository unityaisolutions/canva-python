# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .sort_by_type import SortByType
from .ownership_type import OwnershipType

__all__ = ["BrandTemplateListParams"]


class BrandTemplateListParams(TypedDict, total=False):
    continuation: str
    """
    If the success response contains a continuation token, the user has access to
    more brand templates you can list. You can use this token as a query parameter
    and retrieve more templates from the list, for example
    `/v1/brand-templates?continuation={continuation}`. To retrieve all the brand
    templates available to the user, you might need to make multiple requests.
    """

    dataset: Literal["any", "non_empty"]
    """
    Filter the list of brand templates based on the brand templates' dataset
    definitions. Brand templates with dataset definitions are mainly used with the
    [Autofill APIs](https://www.canva.dev/docs/connect/api-reference/autofills/).

    - `any` - Brand templates with and without dataset definitions.
    - `non_empty` - Brand templates with one or more data fields defined.
    """

    ownership: OwnershipType
    """
    Filter the list of brand templates based on the user's ownership of the brand
    templates.
    """

    query: str
    """
    Lets you search the brand templates available to the user using a search term or
    terms.
    """

    sort_by: SortByType
    """Sort the list of brand templates."""
