from typing import Dict, Tuple
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import authentication

from service_token_authenticator.pydantic_models import ExternalServiceUser

from . import exceptions

# from authtoken.models import Token


class ServiceTokenAuthentication(authentication.BaseAuthentication):

    keyword: str = "Token"  # Bearer

    def get_keyword(self) -> str:
        if hasattr(settings, "SERVICE_TOKEN_KEYWORD") and getattr(
            settings, "SERVICE_TOKEN_KEYWORD", None
        ):
            return settings.SERVICE_TOKEN_KEYWORD
        return self.keyword

    def get_token_mapping(self) -> Dict[str, str]:
        """
        This method should return a mapping <token>: <service_name>
        example:
        SERVICE_TOKEN_MAPPING = {
            "token-one": "service-one"
        }

        We recommend using a code as the name of the service
         in order to associate logics to it,
         such as permissions differentiated by service.
        """
        if settings.SERVICE_TOKEN_MAPPING:
            return settings.SERVICE_TOKEN_MAPPING
        raise exceptions.AuthenticationClassImproperlyConfigured(
            _("Variable SERVICE_TOKEN_MAPPING not configured!")
        )

    def authenticate_header(self, request) -> str:
        return self.get_keyword()

    def authenticate(self, request) -> Tuple[ExternalServiceUser, str]:
        auth = authentication.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.get_keyword().lower().encode():
            msg = _("Invalid authorization header")
            raise exceptions.ExternalServiceAuthenticationFailed(msg)

        if len(auth) == 1:
            msg = _("Invalid basic header. No credentials provided.")
            raise exceptions.ExternalServiceAuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _(
                "Invalid basic header. Credentials string should not contain spaces."
            )
            raise exceptions.ExternalServiceAuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _("Invalid basic header. Credentials not correctly encoded.")
            raise exceptions.ExternalServiceAuthenticationFailed(msg)

        try:
            return self.validate_token(token)
        except exceptions.TokenDoesNotExist:
            raise exceptions.ExternalServiceAuthenticationFailed(msg)

    def validate_token(self, token: str) -> Tuple[ExternalServiceUser, str]:
        token_mapping = self.get_token_mapping()
        if token_mapping.get(token, None):
            return (
                ExternalServiceUser(
                    username=token_mapping.get(token), is_authenticated=True
                ),
                token,
            )
        msg = _("Invalid token. No external service with the token sent")
        raise exceptions.ExternalServiceAuthenticationFailed(msg)
