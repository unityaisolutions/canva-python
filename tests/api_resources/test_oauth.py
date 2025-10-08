# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from canva import Canva, AsyncCanva
from canva.types import (
    OAuthCreateTokenResponse,
    OAuthIntrospectTokenResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_token_overload_1(self, client: Canva) -> None:
        oauth = client.oauth.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_token_with_all_params_overload_1(self, client: Canva) -> None:
        oauth = client.oauth.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
            redirect_uri="https://example.com/process-auth",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_token_overload_1(self, client: Canva) -> None:
        response = client.oauth.with_raw_response.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_token_overload_1(self, client: Canva) -> None:
        with client.oauth.with_streaming_response.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_token_overload_2(self, client: Canva) -> None:
        oauth = client.oauth.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_token_with_all_params_overload_2(self, client: Canva) -> None:
        oauth = client.oauth.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
            scope="design:meta:read",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_token_overload_2(self, client: Canva) -> None:
        response = client.oauth.with_raw_response.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_token_overload_2(self, client: Canva) -> None:
        with client.oauth.with_streaming_response.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_introspect_token(self, client: Canva) -> None:
        oauth = client.oauth.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_introspect_token_with_all_params(self, client: Canva) -> None:
        oauth = client.oauth.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
        )
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_introspect_token(self, client: Canva) -> None:
        response = client.oauth.with_raw_response.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_introspect_token(self, client: Canva) -> None:
        with client.oauth.with_streaming_response.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revoke_token(self, client: Canva) -> None:
        oauth = client.oauth.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )
        assert_matches_type(object, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revoke_token_with_all_params(self, client: Canva) -> None:
        oauth = client.oauth.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
        )
        assert_matches_type(object, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revoke_token(self, client: Canva) -> None:
        response = client.oauth.with_raw_response.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(object, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revoke_token(self, client: Canva) -> None:
        with client.oauth.with_streaming_response.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(object, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_token_overload_1(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_token_with_all_params_overload_1(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
            redirect_uri="https://example.com/process-auth",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_token_overload_1(self, async_client: AsyncCanva) -> None:
        response = await async_client.oauth.with_raw_response.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_token_overload_1(self, async_client: AsyncCanva) -> None:
        async with async_client.oauth.with_streaming_response.create_token(
            code="kp8nnroja7qnx00.opyc1p76rcbyflsxbycjqfp3ub8vzsvltpzwafy9q5l45dn5fxzhe7i7a6mg1i2t8jpsa6sebdeumkzzhicskabgevrxsssec4dvjwfvhq4gs3ugghguar0voiqpfb7axsapiojoter8v3w2s5s3st84jpv2l06h667iw241xngy9c8=vu1tnjp7sz",
            code_verifier="i541qdcfkb4htnork0w92lnu43en99ls5a48ittv6udqgiflqon8vusojojakbq4",
            grant_type="authorization_code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_token_overload_2(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_token_with_all_params_overload_2(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
            scope="design:meta:read",
        )
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_token_overload_2(self, async_client: AsyncCanva) -> None:
        response = await async_client.oauth.with_raw_response.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_token_overload_2(self, async_client: AsyncCanva) -> None:
        async with async_client.oauth.with_streaming_response.create_token(
            grant_type="refresh_token",
            refresh_token="JABix5nolsk9k8n2r0f8nq1gw4zjo40ht6sb4i573wgdzmkwdmiy6muh897hp0bxyab276wtgqkvtob2mg9aidt5d6rcltcbcgs101",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthCreateTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_introspect_token(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_introspect_token_with_all_params(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
        )
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_introspect_token(self, async_client: AsyncCanva) -> None:
        response = await async_client.oauth.with_raw_response.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_introspect_token(self, async_client: AsyncCanva) -> None:
        async with async_client.oauth.with_streaming_response.introspect_token(
            token="JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthIntrospectTokenResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revoke_token(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )
        assert_matches_type(object, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revoke_token_with_all_params(self, async_client: AsyncCanva) -> None:
        oauth = await async_client.oauth.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
            client_id="OC-FAB12-AbCdEf",
            client_secret="cnvcaAbcdefg12345_hijklm6789",
        )
        assert_matches_type(object, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revoke_token(self, async_client: AsyncCanva) -> None:
        response = await async_client.oauth.with_raw_response.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(object, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_token(self, async_client: AsyncCanva) -> None:
        async with async_client.oauth.with_streaming_response.revoke_token(
            token="agALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206ZwxNF4E1y3xKJKF7TzN17BXTfaNOeY0P88AeRCE6cRF7SJzvf3Sx97rA80sGHtFplFo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(object, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True
