from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from controllers.books_controller import BooksController
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    book_controller = BooksController()

    def add_book(self, request):
        self.book_controller.add_book(request.data)
        return self.list(request)

    def remove_book(self, request):
        self.book_controller.remove_book()
        return self.list(request)

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        query_params = request.query_params
        old_name = query_params['old_name']
        new_name = query_params['new_name']
        if old_name and new_name:
            self.book_controller.update_book(old_name, new_name)

        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
