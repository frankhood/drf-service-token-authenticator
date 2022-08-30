import factory

from tests.example.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    isbn = factory.Faker("isbn13")
    author_names = factory.Faker("paragraph")

    class Meta:
        model = Book
