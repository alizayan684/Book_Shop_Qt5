from PyQt5 import QtCore, QtGui, QtWidgets

from Library import *


class Ui_MainWindow(object):
    def __init__(self):
        self.add_book_page = None
        self.price_Bar = None
        self.author_Bar = None
        self.section_Bar = None
        self.name_Bar = None
        self.Buy_Direct = None
        self.profit_Button = None
        self.details_Button = None
        self.label = None
        self.tableWidget = None
        self.Sold = None
        self.Search_comboBox = None
        self.Buy_Button = None
        self.Search_Button = None
        self.Search_Bar = None
        self.Search_Results = None
        self.Search = None
        self.Book_Details_List = None
        self.Library_list = None
        self.toolBox = None
        self.Library = None
        self.LIBRARY_MainWindow = None
        self.central_widget = None
        self.Library_page = None
        self.Book_Details_page = None
        self.library = Library("Ali")

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("MainWindow")
        Main_Window.resize(737, 484)
        # main window
        self.central_widget = QtWidgets.QWidget(Main_Window)
        self.central_widget.setObjectName("central-widget")
        # library Tab
        self.Library = QtWidgets.QWidget()
        self.Library.setObjectName("Library")
        # search Tab
        self.Search = QtWidgets.QWidget()
        self.Search.setObjectName("Search")
        # sold Tab
        self.Sold = QtWidgets.QWidget()
        self.Sold.setObjectName("Sold")

        self.LIBRARY_MainWindow = QtWidgets.QTabWidget(self.central_widget)
        self.LIBRARY_MainWindow.setGeometry(QtCore.QRect(0, 0, 731, 461))
        self.LIBRARY_MainWindow.setObjectName("LIBRARY_MainWindow")

        self.LIBRARY_MainWindow.addTab(self.Library, "")
        self.LIBRARY_MainWindow.addTab(self.Search, "")
        self.LIBRARY_MainWindow.addTab(self.Sold, "")

        ############################################################################
        # Library tool box page
        self.Library_page = QtWidgets.QWidget()
        self.Library_page.setGeometry(QtCore.QRect(0, 0, 691, 331))
        self.Library_page.setObjectName("Library_page")
        # Library list
        self.Library_list = QtWidgets.QListWidget(self.Library_page)
        self.Library_list.setGeometry(QtCore.QRect(40, 11, 611, 281))
        self.Library_list.setObjectName("Library_list")
        data = self.library.get_sections()
        for section in data:
            for book in section.show_books():
                self.Library_list.addItem(book.get_title())

        self.details_Button = QtWidgets.QPushButton(self.Library_page, clicked=lambda: self.show_book_details())
        self.details_Button.setGeometry(QtCore.QRect(500, 10, 151, 31))
        self.details_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.details_Button.setObjectName("details_Button")

        self.delete_Button = QtWidgets.QPushButton(self.Library_page, clicked=lambda: self.delete())
        self.delete_Button.setGeometry(QtCore.QRect(500, 72, 151, 31))
        self.delete_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_Button.setObjectName("delete")

        self.profit_Button = QtWidgets.QPushButton(self.Library_page, clicked=lambda: self.show_profit_details())
        self.profit_Button.setGeometry(QtCore.QRect(500, 41, 151, 31))
        self.profit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profit_Button.setObjectName("profit_Button")

        #######################################################################################
        # Book details tool box page
        self.Book_Details_page = QtWidgets.QWidget()
        self.Book_Details_page.setGeometry(QtCore.QRect(0, 0, 691, 331))
        self.Book_Details_page.setObjectName("Book_Details_page")

        self.Book_Details_List = QtWidgets.QListWidget(self.Book_Details_page)
        self.Book_Details_List.setGeometry(QtCore.QRect(50, 20, 581, 271))
        self.Book_Details_List.setObjectName("Book_Details_List")
        # buy directly button
        self.Buy_Direct = QtWidgets.QPushButton(self.Book_Details_page, clicked=lambda: self.buy_directly())
        self.Buy_Direct.setGeometry(QtCore.QRect(480, 20, 151, 31))
        self.Buy_Direct.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buy_Direct.setObjectName("Buy_Direct")

        #######################################################################################
        # add book tool box page
        self.add_book_page = QtWidgets.QWidget()
        self.add_book_page.setGeometry(QtCore.QRect(0, 0, 691, 331))
        self.add_book_page.setObjectName("add_book")

        self.name_Bar = QtWidgets.QLineEdit(self.add_book_page)
        self.name_Bar.setGeometry(QtCore.QRect(150, 51, 421, 30))
        self.name_Bar.setObjectName("name_Bar")

        self.author_Bar = QtWidgets.QLineEdit(self.add_book_page)
        self.author_Bar.setGeometry(QtCore.QRect(150, 81, 421, 30))
        self.author_Bar.setObjectName("author_Bar")

        self.section_Bar = QtWidgets.QLineEdit(self.add_book_page)
        self.section_Bar.setGeometry(QtCore.QRect(150, 111, 421, 30))
        self.section_Bar.setObjectName("section_Bar")

        self.price_Bar = QtWidgets.QLineEdit(self.add_book_page)
        self.price_Bar.setGeometry(QtCore.QRect(150, 141, 421, 30))
        self.price_Bar.setObjectName("price_Bar")

        self.add_Button = QtWidgets.QPushButton(self.add_book_page,
                                                clicked=lambda: self.add_book())
        self.add_Button.setGeometry(QtCore.QRect(420, 20, 151, 31))
        self.add_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_Button.setObjectName("add_Button")

        #################################################################################
        #tool box
        self.toolBox = QtWidgets.QToolBox(self.Library)
        self.toolBox.setGeometry(QtCore.QRect(20, 14, 691, 391))
        self.toolBox.setObjectName("toolBox")
        self.toolBox.addItem(self.Library_page, "")
        self.toolBox.addItem(self.Book_Details_page, "")
        self.toolBox.addItem(self.add_book_page, "")

        #################################################################################

        self.Search_Results = QtWidgets.QListWidget(self.Search)
        self.Search_Results.setGeometry(QtCore.QRect(80, 111, 571, 271))
        self.Search_Results.setObjectName("Search_Results")

        self.Search_Bar = QtWidgets.QLineEdit(self.Search)
        self.Search_Bar.setGeometry(QtCore.QRect(80, 51, 421, 61))
        self.Search_Bar.setObjectName("Search_Bar")

        self.Search_Button = QtWidgets.QPushButton(self.Search,
                                                   clicked=lambda: self.search_for_book(self.Search_Bar.text()))
        self.Search_Button.setGeometry(QtCore.QRect(500, 50, 151, 31))
        self.Search_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search_Button.setObjectName("Search_Button")

        self.Buy_Button = QtWidgets.QPushButton(self.Search,
                                                clicked=lambda: self.search_and_buy(self.Search_Bar.text()))
        self.Buy_Button.setGeometry(QtCore.QRect(500, 80, 151, 31))
        self.Buy_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buy_Button.setObjectName("Buy_Button")

        self.Search_comboBox = QtWidgets.QComboBox(self.Search)
        self.Search_comboBox.setGeometry(QtCore.QRect(80, 20, 151, 31))
        self.Search_comboBox.setObjectName("comboBox")
        self.Search_comboBox.addItem("Author")
        self.Search_comboBox.addItem("Title")
        self.Search_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ###############################################################################

        self.tableWidget = QtWidgets.QTableWidget(self.Sold)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 750, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.tableWidget.setColumnWidth(0, 280)
        self.tableWidget.setColumnWidth(2, 190)

        self.label = QtWidgets.QLabel(self.Sold)
        self.label.setGeometry(QtCore.QRect(190, 30, 551, 41))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setObjectName("label")

        Main_Window.setCentralWidget(self.central_widget)
        self.translateUi(Main_Window)
        self.LIBRARY_MainWindow.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def translateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.LIBRARY_MainWindow.setTabText(self.LIBRARY_MainWindow.indexOf(self.Library),
                                           _translate("MainWindow", "Library"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Library_page), _translate("MainWindow", "Library Details"))
        self.details_Button.setText(_translate("MainWindow", "Details"))
        self.profit_Button.setText(_translate("MainWindow", "Total Profit"))
        self.delete_Button.setText(_translate("MainWindow", "Delete"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.Book_Details_page), _translate("MainWindow", "Book Details"))
        self.Buy_Direct.setText(_translate("MainWindow", "Buy directly"))

        self.toolBox.setItemText(self.toolBox.indexOf(self.add_book_page), _translate("MainWindow", "Add (title, "
                                                                                                    "author, section,"
                                                                                                    "price) "
                                                                                                    "respectively"))
        self.add_Button.setText(_translate("MainWindow", "Add now!"))

        self.LIBRARY_MainWindow.setTabText(self.LIBRARY_MainWindow.indexOf(self.Search),
                                           _translate("MainWindow", "Search/buy"))
        self.Search_Button.setText(_translate("MainWindow", "Search"))
        self.Buy_Button.setText(_translate("MainWindow", "Buy"))

        self.LIBRARY_MainWindow.setTabText(self.LIBRARY_MainWindow.indexOf(self.Sold), _translate("MainWindow", "Sold"))
        self.label.setText(_translate("MainWindow", "Bought books appear here!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Section"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))

    def show_book_details(self):
        self.Book_Details_List.clear()
        clicked = self.Library_list.currentRow()
        if clicked != -1:
            book_title = self.Library_list.currentItem().text()
            self.toolBox.setCurrentIndex(1)
            book = self.library.search_book_by_title(book_title)
            self.Book_Details_List.addItem("Title: " + book_title)
            self.Book_Details_List.addItem("Author: " + book.get_author())
            self.Book_Details_List.addItem("Section: " + book.get_section())
            self.Book_Details_List.addItem("Price: " + str(book.get_cost()))

    def search_for_book(self, text):
        self.Search_Results.clear()
        if self.Search_comboBox.currentText() == "Author":
            result = self.library.search_book_by_author(text)
            if len(result) == 0:
                self.Search_Results.addItem("No results found!")
            else:
                for i in result:
                    self.Search_Results.addItem("Title: " + i.get_title())
                    self.Search_Results.addItem("Author: " + i.get_author())
                    self.Search_Results.addItem("Price: " + str(i.get_cost()))
                    self.Search_Results.addItem("-----------------------------")
        elif self.Search_comboBox.currentText() == "Title":
            result2 = self.library.search_book_by_title(text)
            if result2 is not None:
                self.Search_Results.addItem("Title: " + result2.get_title())
                self.Search_Results.addItem("Author: " + result2.get_author())
                self.Search_Results.addItem("Price: " + str(result2.get_cost()))
            else:
                self.Search_Results.addItem("No results found!")

    def search_and_buy(self, text1):
        self.Search_Results.clear()
        bought = self.library.search_book_by_title(text1)
        if bought is not None:
            self.library.sell_book(bought.get_title())
            for i in range(self.Library_list.count()):
                item = self.Library_list.item(i).text()
                if item == text1:
                    self.Library_list.takeItem(i)
                    break

            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(bought.get_title()))
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(bought.get_author()))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(bought.get_section()))
            self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(bought.get_cost())))
            self.LIBRARY_MainWindow.setCurrentIndex(2)
        else:
            self.Search_Results.addItem("Not Available!")

    def show_profit_details(self):
        self.Book_Details_List.clear()
        self.toolBox.setCurrentIndex(1)
        profit, books = self.library.get_total_profit()
        self.Book_Details_List.addItem("Total Profit: " + str(profit))
        self.Book_Details_List.addItem("Total sold books: " + str(books))

    def buy_directly(self):
        clicked = self.Library_list.currentRow()
        if clicked != -1 and self.Book_Details_List.count() == 4:
            bought = self.library.search_book_by_title(self.Library_list.currentItem().text())
            self.library.sell_book(bought.get_title())
            self.Library_list.takeItem(self.Library_list.currentRow())

            self.tableWidget.insertRow(0)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(bought.get_title()))
            self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(bought.get_author()))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(bought.get_section()))
            self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(bought.get_cost())))

            self.Book_Details_List.clear()
            self.toolBox.setCurrentIndex(0)
            self.LIBRARY_MainWindow.setCurrentIndex(2)

    def add_book(self):
        title = self.name_Bar.text()
        author = self.author_Bar.text()
        sec_title = self.section_Bar.text()
        cost = self.price_Bar.text()
        found = False
        book = Book(title, author, cost, sec_title)
        for i in self.library.get_sections():
            if sec_title == i.get_title():
                found = True
                i.add_book(book)
        if not found:
            section = Section(sec_title)
            self.library.add_section(section)
            section.add_book(book)
        self.Library_list.addItem(title)

    def delete(self):
        clicked = self.Library_list.currentRow()
        if clicked != -1:
            title = self.Library_list.currentItem().text()
            for i in self.library.get_sections():
                i.delete_book(title)
                2
            self.Library_list.takeItem(self.Library_list.currentRow())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
