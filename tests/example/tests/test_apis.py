from django.conf import settings
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from tests.example.factories import BookFactory


# ===================================================================
# ./manage.py test tests.example.tests.test_apis.BookListAPIViewUnitTest
# ===================================================================
class BookListAPIViewUnitTest(APITestCase):
    def setUp(self) -> None:
        self.api_client = APIClient()

    def test_list_ok(self):
        # ===================================================================
        # ./manage.py test tests.example.tests.test_apis.BookListAPIViewUnitTest.test_list_ok
        # ===================================================================
        for x in range(5):
            BookFactory()

        self.api_client.credentials(
            HTTP_AUTHORIZATION=f"Token {settings.FIRST_SERVICE_TOKEN}"
        )
        response = self.api_client.get("/api/v1/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)
        self.assertEqual(
            sorted(response.json()[0].keys()), sorted(["name", "isbn", "author_names"])
        )

    def test_list_403(self):
        # ===================================================================
        # ./manage.py test tests.example.tests.test_apis.BookListAPIViewUnitTest.test_list_403
        # ===================================================================
        for x in range(5):
            BookFactory()

        self.api_client.credentials(
            HTTP_AUTHORIZATION=f"Token {settings.SECOND_SERVICE_TOKEN}"
        )
        response = self.api_client.get("/api/v1/books/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_401(self):
        # ===================================================================
        # ./manage.py test tests.example.tests.test_apis.BookListAPIViewUnitTest.test_list_401
        # ===================================================================
        for x in range(5):
            BookFactory()

        self.api_client.credentials(HTTP_AUTHORIZATION="Token fuffa")
        response = self.api_client.get("/api/v1/books/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
