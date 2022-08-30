from rest_framework import serializers

from tests.example.models import Book


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            "name",
            "isbn",
            "author_names",
        )