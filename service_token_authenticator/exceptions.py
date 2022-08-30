from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException


class ExternalServiceAuthenticationFailed(AuthenticationFailed):
    """Custom exception to catch for special purposes"""

    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Incorrect authentication credentials.')
    default_code = 'authentication_failed'


class API403Exception(APIException):
    status_code = 403


class TokenDoesNotExist(Exception):
    ...


class AuthenticationClassImproperlyConfigured(Exception):
    ...