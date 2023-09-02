# we are going to create a class called Book as a part of our library management system
class Book:
    # this is a constructor
    def __init__(self, title, author, cost, section):
        self.__title = title
        self.__author = author
        self.__cost = cost
        self.__section = section

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_cost(self):
        return self.__cost

    def get_section(self):
        return self.__section
