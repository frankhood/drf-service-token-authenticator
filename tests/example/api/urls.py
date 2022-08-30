from django.urls import path
from . import views as api_views


urlpatterns = [
    path("books/", api_views.BookAPIView.as_view(), name="book_list"),
]