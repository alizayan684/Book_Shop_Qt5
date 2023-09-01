import json
from Section import Section

from Book import Book


def get_sections():
    with open('books.json') as db:
        data = json.load(db)
        sections = []
        for book in data:
            sec = Section(data[book]["section"])
            if sec not in sections:
                sections.append(sec)
            bo = Book(book, data[book]["author"], data[book]["cost"], data[book]["section"])
            sec.add_book(bo)

        db.close()
        return sections


class Library:
    def __init__(self, title):
        self.__title = title
        self.__sections = get_sections()
        self.__profit = 0

    def add_section(self, section):
        for i in self.__sections:
            if i.get_title() == section.get_title():
                return
        self.__sections.append(section)

    def search_book_by_title(self, title):
        for section in self.__sections:
            book = section.search_book_by_title(title)
            if book is not None:
                return book
        return None

    def search_book_by_author(self, author):
        books = []
        for section in self.__sections:
            book = section.search_book_by_author(author)
            books.extend(book)
        return books

    def sell_book(self, title):
        for section in self.__sections:
            book = section.search_book_by_title(title)
            if book is not None:
                self.__profit += book.get_cost()
                section.delete_book(title)
                return

    def get_total_profit(self):
        return self.__profit

    def get_sections(self):
        return self.__sections
