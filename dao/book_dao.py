from book.models import Book
from django.http import HttpResponseNotFound, HttpResponse


class BookDAO:

    def add_book(self, json_object):
        book = Book()
        book.name = json_object['name']
        book.save()  # must be saved to assign id (used to establish a many-to-many relationship)
        book.author.set(json_object['author'])
        book.description = json_object['description']
        book.genre.set(json_object['genre'])
        book.user.set(json_object['user'])
        book.save()

    def update_book(self, old_name, new_name):
        try:
            book = Book.objects.get(name=old_name)
            book.name = new_name
            book.save()
        except Book.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")

    def remove_book(self, name):
        try:
            book = Book.objects.get(name=name)
            book.delete()
            return HttpResponse("<h2>Book deleted</h2>")
        except Book.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")
