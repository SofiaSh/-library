from book.models import Book


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
        book = Book.objects.get(name=old_name)
        book.name = new_name
        book.save()

    def remove_book(self, name):
        book = Book.objects.get(name=name)
        book.delete()
