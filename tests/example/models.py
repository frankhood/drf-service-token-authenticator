from django.db import models

class Book(models.Model):
    name = models.CharField("Name", max_length=500)
    isbn = models.CharField("ISBN", max_length=500)
    author_names = models.TextField("Author names")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return f"{self.name} ({self.author_names})"
