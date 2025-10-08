# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    apps,
    oauth,
    assets,
    connect,
    exports,
    folders,
    imports,
    resizes,
    comments,
    autofills,
    url_imports,
    asset_uploads,
    brand_templates,
    url_asset_uploads,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.users import users
from .resources.designs import designs

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Canva", "AsyncCanva", "Client", "AsyncClient"]


class Canva(SyncAPIClient):
    apps: apps.AppsResource
    assets: assets.AssetsResource
    asset_uploads: asset_uploads.AssetUploadsResource
    url_asset_uploads: url_asset_uploads.URLAssetUploadsResource
    autofills: autofills.AutofillsResource
    brand_templates: brand_templates.BrandTemplatesResource
    comments: comments.CommentsResource
    designs: designs.DesignsResource
    connect: connect.ConnectResource
    imports: imports.ImportsResource
    url_imports: url_imports.URLImportsResource
    exports: exports.ExportsResource
    folders: folders.FoldersResource
    oauth: oauth.OAuthResource
    resizes: resizes.ResizesResource
    users: users.UsersResource
    with_raw_response: CanvaWithRawResponse
    with_streaming_response: CanvaWithStreamedResponse

    # client options
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Canva client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `CANVA_USERNAME`
        - `password` from `CANVA_PASSWORD`
        """
        if username is None:
            username = os.environ.get("CANVA_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("CANVA_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("CANVA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.canva.com/rest"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.apps = apps.AppsResource(self)
        self.assets = assets.AssetsResource(self)
        self.asset_uploads = asset_uploads.AssetUploadsResource(self)
        self.url_asset_uploads = url_asset_uploads.URLAssetUploadsResource(self)
        self.autofills = autofills.AutofillsResource(self)
        self.brand_templates = brand_templates.BrandTemplatesResource(self)
        self.comments = comments.CommentsResource(self)
        self.designs = designs.DesignsResource(self)
        self.connect = connect.ConnectResource(self)
        self.imports = imports.ImportsResource(self)
        self.url_imports = url_imports.URLImportsResource(self)
        self.exports = exports.ExportsResource(self)
        self.folders = folders.FoldersResource(self)
        self.oauth = oauth.OAuthResource(self)
        self.resizes = resizes.ResizesResource(self)
        self.users = users.UsersResource(self)
        self.with_raw_response = CanvaWithRawResponse(self)
        self.with_streaming_response = CanvaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.username and self.password and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the username or password to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCanva(AsyncAPIClient):
    apps: apps.AsyncAppsResource
    assets: assets.AsyncAssetsResource
    asset_uploads: asset_uploads.AsyncAssetUploadsResource
    url_asset_uploads: url_asset_uploads.AsyncURLAssetUploadsResource
    autofills: autofills.AsyncAutofillsResource
    brand_templates: brand_templates.AsyncBrandTemplatesResource
    comments: comments.AsyncCommentsResource
    designs: designs.AsyncDesignsResource
    connect: connect.AsyncConnectResource
    imports: imports.AsyncImportsResource
    url_imports: url_imports.AsyncURLImportsResource
    exports: exports.AsyncExportsResource
    folders: folders.AsyncFoldersResource
    oauth: oauth.AsyncOAuthResource
    resizes: resizes.AsyncResizesResource
    users: users.AsyncUsersResource
    with_raw_response: AsyncCanvaWithRawResponse
    with_streaming_response: AsyncCanvaWithStreamedResponse

    # client options
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCanva client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `username` from `CANVA_USERNAME`
        - `password` from `CANVA_PASSWORD`
        """
        if username is None:
            username = os.environ.get("CANVA_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("CANVA_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("CANVA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.canva.com/rest"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.apps = apps.AsyncAppsResource(self)
        self.assets = assets.AsyncAssetsResource(self)
        self.asset_uploads = asset_uploads.AsyncAssetUploadsResource(self)
        self.url_asset_uploads = url_asset_uploads.AsyncURLAssetUploadsResource(self)
        self.autofills = autofills.AsyncAutofillsResource(self)
        self.brand_templates = brand_templates.AsyncBrandTemplatesResource(self)
        self.comments = comments.AsyncCommentsResource(self)
        self.designs = designs.AsyncDesignsResource(self)
        self.connect = connect.AsyncConnectResource(self)
        self.imports = imports.AsyncImportsResource(self)
        self.url_imports = url_imports.AsyncURLImportsResource(self)
        self.exports = exports.AsyncExportsResource(self)
        self.folders = folders.AsyncFoldersResource(self)
        self.oauth = oauth.AsyncOAuthResource(self)
        self.resizes = resizes.AsyncResizesResource(self)
        self.users = users.AsyncUsersResource(self)
        self.with_raw_response = AsyncCanvaWithRawResponse(self)
        self.with_streaming_response = AsyncCanvaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.username and self.password and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the username or password to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CanvaWithRawResponse:
    def __init__(self, client: Canva) -> None:
        self.apps = apps.AppsResourceWithRawResponse(client.apps)
        self.assets = assets.AssetsResourceWithRawResponse(client.assets)
        self.asset_uploads = asset_uploads.AssetUploadsResourceWithRawResponse(client.asset_uploads)
        self.url_asset_uploads = url_asset_uploads.URLAssetUploadsResourceWithRawResponse(client.url_asset_uploads)
        self.autofills = autofills.AutofillsResourceWithRawResponse(client.autofills)
        self.brand_templates = brand_templates.BrandTemplatesResourceWithRawResponse(client.brand_templates)
        self.comments = comments.CommentsResourceWithRawResponse(client.comments)
        self.designs = designs.DesignsResourceWithRawResponse(client.designs)
        self.connect = connect.ConnectResourceWithRawResponse(client.connect)
        self.imports = imports.ImportsResourceWithRawResponse(client.imports)
        self.url_imports = url_imports.URLImportsResourceWithRawResponse(client.url_imports)
        self.exports = exports.ExportsResourceWithRawResponse(client.exports)
        self.folders = folders.FoldersResourceWithRawResponse(client.folders)
        self.oauth = oauth.OAuthResourceWithRawResponse(client.oauth)
        self.resizes = resizes.ResizesResourceWithRawResponse(client.resizes)
        self.users = users.UsersResourceWithRawResponse(client.users)


class AsyncCanvaWithRawResponse:
    def __init__(self, client: AsyncCanva) -> None:
        self.apps = apps.AsyncAppsResourceWithRawResponse(client.apps)
        self.assets = assets.AsyncAssetsResourceWithRawResponse(client.assets)
        self.asset_uploads = asset_uploads.AsyncAssetUploadsResourceWithRawResponse(client.asset_uploads)
        self.url_asset_uploads = url_asset_uploads.AsyncURLAssetUploadsResourceWithRawResponse(client.url_asset_uploads)
        self.autofills = autofills.AsyncAutofillsResourceWithRawResponse(client.autofills)
        self.brand_templates = brand_templates.AsyncBrandTemplatesResourceWithRawResponse(client.brand_templates)
        self.comments = comments.AsyncCommentsResourceWithRawResponse(client.comments)
        self.designs = designs.AsyncDesignsResourceWithRawResponse(client.designs)
        self.connect = connect.AsyncConnectResourceWithRawResponse(client.connect)
        self.imports = imports.AsyncImportsResourceWithRawResponse(client.imports)
        self.url_imports = url_imports.AsyncURLImportsResourceWithRawResponse(client.url_imports)
        self.exports = exports.AsyncExportsResourceWithRawResponse(client.exports)
        self.folders = folders.AsyncFoldersResourceWithRawResponse(client.folders)
        self.oauth = oauth.AsyncOAuthResourceWithRawResponse(client.oauth)
        self.resizes = resizes.AsyncResizesResourceWithRawResponse(client.resizes)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)


class CanvaWithStreamedResponse:
    def __init__(self, client: Canva) -> None:
        self.apps = apps.AppsResourceWithStreamingResponse(client.apps)
        self.assets = assets.AssetsResourceWithStreamingResponse(client.assets)
        self.asset_uploads = asset_uploads.AssetUploadsResourceWithStreamingResponse(client.asset_uploads)
        self.url_asset_uploads = url_asset_uploads.URLAssetUploadsResourceWithStreamingResponse(
            client.url_asset_uploads
        )
        self.autofills = autofills.AutofillsResourceWithStreamingResponse(client.autofills)
        self.brand_templates = brand_templates.BrandTemplatesResourceWithStreamingResponse(client.brand_templates)
        self.comments = comments.CommentsResourceWithStreamingResponse(client.comments)
        self.designs = designs.DesignsResourceWithStreamingResponse(client.designs)
        self.connect = connect.ConnectResourceWithStreamingResponse(client.connect)
        self.imports = imports.ImportsResourceWithStreamingResponse(client.imports)
        self.url_imports = url_imports.URLImportsResourceWithStreamingResponse(client.url_imports)
        self.exports = exports.ExportsResourceWithStreamingResponse(client.exports)
        self.folders = folders.FoldersResourceWithStreamingResponse(client.folders)
        self.oauth = oauth.OAuthResourceWithStreamingResponse(client.oauth)
        self.resizes = resizes.ResizesResourceWithStreamingResponse(client.resizes)
        self.users = users.UsersResourceWithStreamingResponse(client.users)


class AsyncCanvaWithStreamedResponse:
    def __init__(self, client: AsyncCanva) -> None:
        self.apps = apps.AsyncAppsResourceWithStreamingResponse(client.apps)
        self.assets = assets.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.asset_uploads = asset_uploads.AsyncAssetUploadsResourceWithStreamingResponse(client.asset_uploads)
        self.url_asset_uploads = url_asset_uploads.AsyncURLAssetUploadsResourceWithStreamingResponse(
            client.url_asset_uploads
        )
        self.autofills = autofills.AsyncAutofillsResourceWithStreamingResponse(client.autofills)
        self.brand_templates = brand_templates.AsyncBrandTemplatesResourceWithStreamingResponse(client.brand_templates)
        self.comments = comments.AsyncCommentsResourceWithStreamingResponse(client.comments)
        self.designs = designs.AsyncDesignsResourceWithStreamingResponse(client.designs)
        self.connect = connect.AsyncConnectResourceWithStreamingResponse(client.connect)
        self.imports = imports.AsyncImportsResourceWithStreamingResponse(client.imports)
        self.url_imports = url_imports.AsyncURLImportsResourceWithStreamingResponse(client.url_imports)
        self.exports = exports.AsyncExportsResourceWithStreamingResponse(client.exports)
        self.folders = folders.AsyncFoldersResourceWithStreamingResponse(client.folders)
        self.oauth = oauth.AsyncOAuthResourceWithStreamingResponse(client.oauth)
        self.resizes = resizes.AsyncResizesResourceWithStreamingResponse(client.resizes)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)


Client = Canva

AsyncClient = AsyncCanva
