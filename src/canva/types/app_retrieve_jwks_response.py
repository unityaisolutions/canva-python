# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AppRetrieveJwksResponse", "Key"]


class Key(BaseModel):
    e: str
    """
    The "e" (exponent) parameter contains the exponent value for the RSA public key.
    It is represented as a Base64urlUInt-encoded value. See
    https://www.rfc-editor.org/rfc/rfc7518.html#section-6.3
    """

    kid: str
    """The "kid" (key ID) parameter is used to match a specific key.

    This is used, for instance, to choose among a set of keys within a JWK Set
    during key rollover. When "kid" values are used within a JWK Set, different keys
    within the JWK Set SHOULD use distinct "kid" values. The "kid" value is a
    case-sensitive string. See https://www.rfc-editor.org/rfc/rfc7517#section-4
    """

    kty: str
    """
    The "kty" (key type) parameter identifies the cryptographic algorithm family
    used with the key, such as "RSA" or "EC". The "kty" value is a case-sensitive
    string. At the moment, only "RSA" is supported. See
    https://www.rfc-editor.org/rfc/rfc7517#section-4
    """

    n: str
    """The "n" (modulus) parameter contains the modulus value for the RSA public key.

    It is represented as a Base64urlUInt-encoded value. See
    https://www.rfc-editor.org/rfc/rfc7518.html#section-6.3
    """

    alg: Optional[str] = None
    """
    The "alg" (algorithm) parameter identifies the algorithm intended for use with
    the key. See https://www.rfc-editor.org/rfc/rfc7517#section-4
    """

    use: Optional[str] = None
    """
    The "use" (public key use) parameter identifies the intended use of the public
    key. The "use" parameter is employed to indicate whether a public key is used
    for encrypting data or verifying the signature on data. Values are commonly
    "sig" (signature) or "enc" (encryption). See
    https://www.rfc-editor.org/rfc/rfc7517#section-4
    """


class AppRetrieveJwksResponse(BaseModel):
    keys: List[Key]
    """The value of the "keys" parameter is an array of JWK values.

    The order of keys has no meaning.
    """
