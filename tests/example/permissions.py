from typing import List
from service_token_authenticator.permission_mixins import IsExternalServicePermissionMixin
from django.conf import settings


class IsFirstServicePermission(IsExternalServicePermissionMixin):
    def get_external_service_codes(self) -> List[str]:
        return [settings.FIRST_SERVICE_USERNAME]