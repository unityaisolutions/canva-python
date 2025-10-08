# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PresetDesignTypeInputParam"]


class PresetDesignTypeInputParam(TypedDict, total=False):
    name: Required[Literal["doc", "whiteboard", "presentation"]]
    """The name of the design type.

    - `doc` - A [Canva doc](https://www.canva.com/docs/); a document for Canva's
      online text editor.
    - `whiteboard` - A [whiteboard](https://www.canva.com/online-whiteboard/); a
      design which gives you infinite space to collaborate.
    - `presentation` - A [presentation](https://www.canva.com/presentations/); lets
      you create and collaborate for presenting to an audience.
    """

    type: Required[Literal["preset"]]
