# Shared Types

```python
from canva.types import TeamUser
```

# Apps

Types:

```python
from canva.types import AppRetrieveJwksResponse
```

Methods:

- <code title="get /v1/apps/{appId}/jwks">client.apps.<a href="./src/canva/resources/apps.py">retrieve_jwks</a>(app_id) -> <a href="./src/canva/types/app_retrieve_jwks_response.py">AppRetrieveJwksResponse</a></code>

# Assets

Types:

```python
from canva.types import Asset, AssetType, Thumbnail, AssetRetrieveResponse, AssetUpdateResponse
```

Methods:

- <code title="get /v1/assets/{assetId}">client.assets.<a href="./src/canva/resources/assets.py">retrieve</a>(asset_id) -> <a href="./src/canva/types/asset_retrieve_response.py">AssetRetrieveResponse</a></code>
- <code title="patch /v1/assets/{assetId}">client.assets.<a href="./src/canva/resources/assets.py">update</a>(asset_id, \*\*<a href="src/canva/types/asset_update_params.py">params</a>) -> <a href="./src/canva/types/asset_update_response.py">AssetUpdateResponse</a></code>
- <code title="delete /v1/assets/{assetId}">client.assets.<a href="./src/canva/resources/assets.py">delete</a>(asset_id) -> None</code>

# AssetUploads

Types:

```python
from canva.types import AssetUploadJob, AssetUploadCreateResponse, AssetUploadRetrieveResponse
```

Methods:

- <code title="post /v1/asset-uploads">client.asset_uploads.<a href="./src/canva/resources/asset_uploads.py">create</a>(body, \*\*<a href="src/canva/types/asset_upload_create_params.py">params</a>) -> <a href="./src/canva/types/asset_upload_create_response.py">AssetUploadCreateResponse</a></code>
- <code title="get /v1/asset-uploads/{jobId}">client.asset_uploads.<a href="./src/canva/resources/asset_uploads.py">retrieve</a>(job_id) -> <a href="./src/canva/types/asset_upload_retrieve_response.py">AssetUploadRetrieveResponse</a></code>

# URLAssetUploads

Types:

```python
from canva.types import URLAssetUploadCreateResponse, URLAssetUploadRetrieveResponse
```

Methods:

- <code title="post /v1/url-asset-uploads">client.url_asset_uploads.<a href="./src/canva/resources/url_asset_uploads.py">create</a>(\*\*<a href="src/canva/types/url_asset_upload_create_params.py">params</a>) -> <a href="./src/canva/types/url_asset_upload_create_response.py">URLAssetUploadCreateResponse</a></code>
- <code title="get /v1/url-asset-uploads/{jobId}">client.url_asset_uploads.<a href="./src/canva/resources/url_asset_uploads.py">retrieve</a>(job_id) -> <a href="./src/canva/types/url_asset_upload_retrieve_response.py">URLAssetUploadRetrieveResponse</a></code>

# Autofills

Types:

```python
from canva.types import DesignAutofillJob, AutofillCreateResponse, AutofillRetrieveResponse
```

Methods:

- <code title="post /v1/autofills">client.autofills.<a href="./src/canva/resources/autofills.py">create</a>(\*\*<a href="src/canva/types/autofill_create_params.py">params</a>) -> <a href="./src/canva/types/autofill_create_response.py">AutofillCreateResponse</a></code>
- <code title="get /v1/autofills/{jobId}">client.autofills.<a href="./src/canva/resources/autofills.py">retrieve</a>(job_id) -> <a href="./src/canva/types/autofill_retrieve_response.py">AutofillRetrieveResponse</a></code>

# BrandTemplates

Types:

```python
from canva.types import (
    BrandTemplate,
    OwnershipType,
    SortByType,
    BrandTemplateRetrieveResponse,
    BrandTemplateListResponse,
    BrandTemplateRetrieveDatasetResponse,
)
```

Methods:

- <code title="get /v1/brand-templates/{brandTemplateId}">client.brand_templates.<a href="./src/canva/resources/brand_templates.py">retrieve</a>(brand_template_id) -> <a href="./src/canva/types/brand_template_retrieve_response.py">BrandTemplateRetrieveResponse</a></code>
- <code title="get /v1/brand-templates">client.brand_templates.<a href="./src/canva/resources/brand_templates.py">list</a>(\*\*<a href="src/canva/types/brand_template_list_params.py">params</a>) -> <a href="./src/canva/types/brand_template_list_response.py">BrandTemplateListResponse</a></code>
- <code title="get /v1/brand-templates/{brandTemplateId}/dataset">client.brand_templates.<a href="./src/canva/resources/brand_templates.py">retrieve_dataset</a>(brand_template_id) -> <a href="./src/canva/types/brand_template_retrieve_dataset_response.py">BrandTemplateRetrieveDatasetResponse</a></code>

# Comments

Types:

```python
from canva.types import (
    CommentObject,
    CommentObjectInput,
    ParentComment,
    ReplyComment,
    User,
    CommentCreateReplyResponse,
    CommentCreateThreadResponse,
)
```

Methods:

- <code title="post /v1/comments/{commentId}/replies">client.comments.<a href="./src/canva/resources/comments.py">create_reply</a>(comment_id, \*\*<a href="src/canva/types/comment_create_reply_params.py">params</a>) -> <a href="./src/canva/types/comment_create_reply_response.py">CommentCreateReplyResponse</a></code>
- <code title="post /v1/comments">client.comments.<a href="./src/canva/resources/comments.py">create_thread</a>(\*\*<a href="src/canva/types/comment_create_thread_params.py">params</a>) -> <a href="./src/canva/types/comment_create_thread_response.py">CommentCreateThreadResponse</a></code>

# Designs

Types:

```python
from canva.types import (
    CustomDesignTypeInput,
    Design,
    DesignLinks,
    DesignTypeInput,
    PresetDesignTypeInput,
    DesignCreateResponse,
    DesignRetrieveResponse,
    DesignListResponse,
)
```

Methods:

- <code title="post /v1/designs">client.designs.<a href="./src/canva/resources/designs/designs.py">create</a>(\*\*<a href="src/canva/types/design_create_params.py">params</a>) -> <a href="./src/canva/types/design_create_response.py">DesignCreateResponse</a></code>
- <code title="get /v1/designs/{designId}">client.designs.<a href="./src/canva/resources/designs/designs.py">retrieve</a>(design_id) -> <a href="./src/canva/types/design_retrieve_response.py">DesignRetrieveResponse</a></code>
- <code title="get /v1/designs">client.designs.<a href="./src/canva/resources/designs/designs.py">list</a>(\*\*<a href="src/canva/types/design_list_params.py">params</a>) -> <a href="./src/canva/types/design_list_response.py">DesignListResponse</a></code>

## Comments

Types:

```python
from canva.types.designs import Thread, CommentCreateResponse, CommentRetrieveResponse
```

Methods:

- <code title="post /v1/designs/{designId}/comments">client.designs.comments.<a href="./src/canva/resources/designs/comments/comments.py">create</a>(design_id, \*\*<a href="src/canva/types/designs/comment_create_params.py">params</a>) -> <a href="./src/canva/types/designs/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="get /v1/designs/{designId}/comments/{threadId}">client.designs.comments.<a href="./src/canva/resources/designs/comments/comments.py">retrieve</a>(thread_id, \*, design_id) -> <a href="./src/canva/types/designs/comment_retrieve_response.py">CommentRetrieveResponse</a></code>

### Replies

Types:

```python
from canva.types.designs.comments import (
    CommentContent,
    Reply,
    ReplyCreateResponse,
    ReplyRetrieveResponse,
    ReplyListResponse,
)
```

Methods:

- <code title="post /v1/designs/{designId}/comments/{threadId}/replies">client.designs.comments.replies.<a href="./src/canva/resources/designs/comments/replies.py">create</a>(thread_id, \*, design_id, \*\*<a href="src/canva/types/designs/comments/reply_create_params.py">params</a>) -> <a href="./src/canva/types/designs/comments/reply_create_response.py">ReplyCreateResponse</a></code>
- <code title="get /v1/designs/{designId}/comments/{threadId}/replies/{replyId}">client.designs.comments.replies.<a href="./src/canva/resources/designs/comments/replies.py">retrieve</a>(reply_id, \*, design_id, thread_id) -> <a href="./src/canva/types/designs/comments/reply_retrieve_response.py">ReplyRetrieveResponse</a></code>
- <code title="get /v1/designs/{designId}/comments/{threadId}/replies">client.designs.comments.replies.<a href="./src/canva/resources/designs/comments/replies.py">list</a>(thread_id, \*, design_id, \*\*<a href="src/canva/types/designs/comments/reply_list_params.py">params</a>) -> <a href="./src/canva/types/designs/comments/reply_list_response.py">ReplyListResponse</a></code>

## Pages

Types:

```python
from canva.types.designs import PageRetrieveResponse
```

Methods:

- <code title="get /v1/designs/{designId}/pages">client.designs.pages.<a href="./src/canva/resources/designs/pages.py">retrieve</a>(design_id, \*\*<a href="src/canva/types/designs/page_retrieve_params.py">params</a>) -> <a href="./src/canva/types/designs/page_retrieve_response.py">PageRetrieveResponse</a></code>

## ExportFormats

Types:

```python
from canva.types.designs import ExportFormatRetrieveResponse
```

Methods:

- <code title="get /v1/designs/{designId}/export-formats">client.designs.export_formats.<a href="./src/canva/resources/designs/export_formats.py">retrieve</a>(design_id) -> <a href="./src/canva/types/designs/export_format_retrieve_response.py">ExportFormatRetrieveResponse</a></code>

# Connect

Types:

```python
from canva.types import ConnectRetrieveKeysResponse
```

Methods:

- <code title="get /v1/connect/keys">client.connect.<a href="./src/canva/resources/connect.py">retrieve_keys</a>() -> <a href="./src/canva/types/connect_retrieve_keys_response.py">ConnectRetrieveKeysResponse</a></code>

# Imports

Types:

```python
from canva.types import DesignImportJob, ImportCreateResponse, ImportRetrieveResponse
```

Methods:

- <code title="post /v1/imports">client.imports.<a href="./src/canva/resources/imports.py">create</a>(body, \*\*<a href="src/canva/types/import_create_params.py">params</a>) -> <a href="./src/canva/types/import_create_response.py">ImportCreateResponse</a></code>
- <code title="get /v1/imports/{jobId}">client.imports.<a href="./src/canva/resources/imports.py">retrieve</a>(job_id) -> <a href="./src/canva/types/import_retrieve_response.py">ImportRetrieveResponse</a></code>

# URLImports

Types:

```python
from canva.types import URLImportCreateResponse, URLImportRetrieveResponse
```

Methods:

- <code title="post /v1/url-imports">client.url_imports.<a href="./src/canva/resources/url_imports.py">create</a>(\*\*<a href="src/canva/types/url_import_create_params.py">params</a>) -> <a href="./src/canva/types/url_import_create_response.py">URLImportCreateResponse</a></code>
- <code title="get /v1/url-imports/{jobId}">client.url_imports.<a href="./src/canva/resources/url_imports.py">retrieve</a>(job_id) -> <a href="./src/canva/types/url_import_retrieve_response.py">URLImportRetrieveResponse</a></code>

# Exports

Types:

```python
from canva.types import ExportJob, ExportQuality, ExportCreateResponse, ExportRetrieveResponse
```

Methods:

- <code title="post /v1/exports">client.exports.<a href="./src/canva/resources/exports.py">create</a>(\*\*<a href="src/canva/types/export_create_params.py">params</a>) -> <a href="./src/canva/types/export_create_response.py">ExportCreateResponse</a></code>
- <code title="get /v1/exports/{exportId}">client.exports.<a href="./src/canva/resources/exports.py">retrieve</a>(export_id) -> <a href="./src/canva/types/export_retrieve_response.py">ExportRetrieveResponse</a></code>

# Folders

Types:

```python
from canva.types import (
    Folder,
    FolderCreateResponse,
    FolderRetrieveResponse,
    FolderUpdateResponse,
    FolderListItemsResponse,
)
```

Methods:

- <code title="post /v1/folders">client.folders.<a href="./src/canva/resources/folders.py">create</a>(\*\*<a href="src/canva/types/folder_create_params.py">params</a>) -> <a href="./src/canva/types/folder_create_response.py">FolderCreateResponse</a></code>
- <code title="get /v1/folders/{folderId}">client.folders.<a href="./src/canva/resources/folders.py">retrieve</a>(folder_id) -> <a href="./src/canva/types/folder_retrieve_response.py">FolderRetrieveResponse</a></code>
- <code title="patch /v1/folders/{folderId}">client.folders.<a href="./src/canva/resources/folders.py">update</a>(folder_id, \*\*<a href="src/canva/types/folder_update_params.py">params</a>) -> <a href="./src/canva/types/folder_update_response.py">FolderUpdateResponse</a></code>
- <code title="delete /v1/folders/{folderId}">client.folders.<a href="./src/canva/resources/folders.py">delete</a>(folder_id) -> None</code>
- <code title="get /v1/folders/{folderId}/items">client.folders.<a href="./src/canva/resources/folders.py">list_items</a>(folder_id, \*\*<a href="src/canva/types/folder_list_items_params.py">params</a>) -> <a href="./src/canva/types/folder_list_items_response.py">FolderListItemsResponse</a></code>
- <code title="post /v1/folders/move">client.folders.<a href="./src/canva/resources/folders.py">move_item</a>(\*\*<a href="src/canva/types/folder_move_item_params.py">params</a>) -> None</code>

# OAuth

Types:

```python
from canva.types import OAuthCreateTokenResponse, OAuthIntrospectTokenResponse
```

Methods:

- <code title="post /v1/oauth/token">client.oauth.<a href="./src/canva/resources/oauth.py">create_token</a>(\*\*<a href="src/canva/types/oauth_create_token_params.py">params</a>) -> <a href="./src/canva/types/oauth_create_token_response.py">OAuthCreateTokenResponse</a></code>
- <code title="post /v1/oauth/introspect">client.oauth.<a href="./src/canva/resources/oauth.py">introspect_token</a>(\*\*<a href="src/canva/types/oauth_introspect_token_params.py">params</a>) -> <a href="./src/canva/types/oauth_introspect_token_response.py">OAuthIntrospectTokenResponse</a></code>
- <code title="post /v1/oauth/revoke">client.oauth.<a href="./src/canva/resources/oauth.py">revoke_token</a>(\*\*<a href="src/canva/types/oauth_revoke_token_params.py">params</a>) -> object</code>

# Resizes

Types:

```python
from canva.types import DesignResizeJob, DesignSummary, ResizeCreateResponse, ResizeRetrieveResponse
```

Methods:

- <code title="post /v1/resizes">client.resizes.<a href="./src/canva/resources/resizes.py">create</a>(\*\*<a href="src/canva/types/resize_create_params.py">params</a>) -> <a href="./src/canva/types/resize_create_response.py">ResizeCreateResponse</a></code>
- <code title="get /v1/resizes/{jobId}">client.resizes.<a href="./src/canva/resources/resizes.py">retrieve</a>(job_id) -> <a href="./src/canva/types/resize_retrieve_response.py">ResizeRetrieveResponse</a></code>

# Users

## Me

Types:

```python
from canva.types.users import (
    TeamUserSummary,
    MeRetrieveResponse,
    MeListCapabilitiesResponse,
    MeRetrieveProfileResponse,
)
```

Methods:

- <code title="get /v1/users/me">client.users.me.<a href="./src/canva/resources/users/me.py">retrieve</a>() -> <a href="./src/canva/types/users/me_retrieve_response.py">MeRetrieveResponse</a></code>
- <code title="get /v1/users/me/capabilities">client.users.me.<a href="./src/canva/resources/users/me.py">list_capabilities</a>() -> <a href="./src/canva/types/users/me_list_capabilities_response.py">MeListCapabilitiesResponse</a></code>
- <code title="get /v1/users/me/profile">client.users.me.<a href="./src/canva/resources/users/me.py">retrieve_profile</a>() -> <a href="./src/canva/types/users/me_retrieve_profile_response.py">MeRetrieveProfileResponse</a></code>
