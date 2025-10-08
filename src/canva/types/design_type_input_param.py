# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .custom_design_type_input_param import CustomDesignTypeInputParam
from .preset_design_type_input_param import PresetDesignTypeInputParam

__all__ = ["DesignTypeInputParam"]

DesignTypeInputParam: TypeAlias = Union[PresetDesignTypeInputParam, CustomDesignTypeInputParam]
