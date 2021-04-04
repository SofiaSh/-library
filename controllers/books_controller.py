from dao.book_dao import BookDAO


class BooksController:
    books_dao = BookDAO()

    def add_book(self, json_object):
        self.books_dao.add_book(json_object)

    def update_book(self, old_name, new_name):
        self.books_dao.update_book(old_name, new_name)

    def remove_book(self, name):
        self.books_dao.remove_book(name)
