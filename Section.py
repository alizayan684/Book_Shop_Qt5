class Section:
    def __init__(self, title):
        self.__title = title
        self.__books = []

    def get_title(self):
        return self.__title

    def add_book(self, book):
        return self.__books.append(book)

    def search_book_by_title(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None

    def search_book_by_author(self, author):
        books = []
        for book in self.__books:
            if book.get_author() == author:
                books.append(book)
        return books

    def delete_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                self.__books.remove(book)

    def show_books(self):
        return self.__books
