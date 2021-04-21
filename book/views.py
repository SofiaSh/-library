from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from controllers.books_controller import BooksController
from django.shortcuts import get_object_or_404
from django.conf import settings
import redis
from rest_framework.response import Response

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    book_controller = BooksController()

    def add_book(self, request):
        self.book_controller.add_book(request.data)
        return self.list(request)

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def update_book(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, pk=None):
        if pk:
            value = redis_instance.get(pk)
            if value:
                redis_instance.set(pk, int(value)+1)
                response = {
                    'key': pk,
                    'value': value,
                    'msg': f"Successfully updated {pk}"
                }
                return Response(response, status=200)
            else:
                redis_instance.set(pk, 0)
                response = {
                    'key': pk,
                    'value': 0,
                    'msg': f"Successfully updated {pk}"
                }
                return Response(response, status=200)
        result = None
        query_params = request.query_params
        if 'old_name' in query_params and 'new_name' in query_params:
            old_name = query_params['old_name']
            new_name = query_params['new_name']
            result = self.book_controller.update_book(old_name, new_name)
        elif 'name' in query_params:
            result = self.book_controller.remove_book(query_params['name'])

        if result:
            return result

        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def get(self, request, pk=None):

        return self.retrieve(request, pk)
