from rest_framework.viewsets import mixins, generics
from tests.example.api.serializers import BookListSerializer

from tests.example.models import Book
from service_token_authenticator.authentication import ServiceTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from tests.example.permissions import IsFirstServicePermission

class BookAPIView(generics.ListAPIView):
    authentication_classes = (ServiceTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsFirstServicePermission,
    )
    serializer_class = BookListSerializer

    def get_queryset(self):
        return Book.objects.all()