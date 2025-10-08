# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ConnectRetrieveKeysResponse", "Key"]


class Key(BaseModel):
    crv: str
    """
    The `crv` (curve) property identifies the curve used for elliptical curve
    encryptions. Only "Ed25519" is supported. For more information on the `crv`
    property, see
    [RFC-8037 — Key Type "OKP"](https://www.rfc-editor.org/rfc/rfc8037.html#section-2).
    """

    kid: str
    """The `kid` (key ID) is a unique identifier for a public key.

    When the keys used to sign webhooks are rotated, you can use this ID to select
    the correct key within a JWK Set during the key rollover. The `kid` value is
    case-sensitive.
    """

    kty: str
    """
    The `kty` (key type) identifies the cryptographic algorithm family used with the
    key, such as "RSA" or "EC". Only Octet Key Pairs (`OKPs`) are supported. The
    `kty` value is case-sensitive. For more information on the `kty` property and
    OKPs, see
    [RFC-8037 — "kty" (Key Type) Parameter](https://www.rfc-editor.org/rfc/rfc8037.html#section-2).
    """

    x: str
    """The `x` property is the public key of an elliptical curve encryption.

    The key is Base64urlUInt-encoded. For more information on the `x` property, see
    [RFC-8037 — "x" (X Coordinate) Parameter](https://www.rfc-editor.org/rfc/rfc8037#section-2).
    """


class ConnectRetrieveKeysResponse(BaseModel):
    keys: List[Key]
    """A Json Web Key Set (JWKS) with public keys used for signing webhooks.

    You can use this JWKS to verify that a webhook was sent from Canva.
    """
