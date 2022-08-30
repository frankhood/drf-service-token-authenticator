from typing import List

from django.utils.translation import ugettext_lazy as _
from rest_framework.permissions import BasePermission

from service_token_authenticator.exceptions import API403Exception


class IsExternalServicePermissionMixin(BasePermission):
    def get_external_service_codes(self) -> List[str]:
        """
        This method should return a list of external services usernames.
        The external service username should match the one in SERVICE_TOKEN_MAPPING variable.
        """
        raise NotImplementedError(".get_external_service_codes() must be overridden.")

    def has_permission(self, request, view) -> bool:
        if request.user.username not in self.get_external_service_codes():
            raise API403Exception(detail=_("Unauthorized"))
        return True
