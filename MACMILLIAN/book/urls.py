from django.urls import path
from .views import display_books, get_single_book, create_single_book, update_single_book


urlpatterns = [
    path("", display_books, name="all_books"),
    # path("<int:id>/", display, name="single_books"),
    path("create/", create_single_book, name="create-book"),
    path("<slug:slug>/update/", update_single_book, name="update-book"),
    path("<slug:slug>/", get_single_book, name="single_book")
]