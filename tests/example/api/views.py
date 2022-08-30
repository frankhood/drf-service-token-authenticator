from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import generics

from service_token_authenticator import authentication
from tests.example.api.serializers import BookListSerializer
from tests.example.models import Book
from tests.example.permissions import IsFirstServicePermission


class BookAPIView(generics.ListAPIView):
    authentication_classes = (authentication.ServiceTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        IsFirstServicePermission,
    )
    serializer_class = BookListSerializer

    def get_queryset(self):
        return Book.objects.all()
