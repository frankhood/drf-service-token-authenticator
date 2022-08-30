from typing import List

from django.conf import settings

from service_token_authenticator import permission_mixins


class IsFirstServicePermission(permission_mixins.IsExternalServicePermissionMixin):
    def get_external_service_codes(self) -> List[str]:
        return [settings.FIRST_SERVICE_USERNAME]
