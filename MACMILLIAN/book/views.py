from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

@api_view(["GET"])
def display_books(request):
    all_books = Book.objects.all()
    serialized_books = BookSerializer(all_books, many=True)
    return Response(serialized_books.data)


# @api_view(["GET"])
# def display(request, id):
#     single_books = Book.objects.get(id=id)
#     serialized_book = BookSerializer(single_books)
#     return Response(serialized_book.data)

@api_view(["GET"])
def get_single_book(request, slug):
    single_book = Book.objects.get(slug)
    serialized_book = BookSerializer(single_book)
    return Response(serialized_book.data)

@api_view(["POST"])
def create_single_book(request):
    new_book = BookSerializer(data=request.data)
    if new_book.is_valid():
        new_book.save()
        return Response("Book creation successful")
    return Response("Something went wrong")


@api_view(["PUT"])
def update_single_book(request, slug):
    single_book = Book.objects.get(slug=slug)
    new_data = BookSerializer(single_book, data=request.data, partial=True)
    if new_data.is_valid():
        new_data.save()
        return Response("Book data has been updated successfully!!")
    return Response(new_data.errors)