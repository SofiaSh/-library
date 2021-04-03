from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#    def perform_create(self, serializer):
   #     serializer.save(author=self.request.user)