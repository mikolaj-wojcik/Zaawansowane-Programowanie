import datetime
from classes import Student as s
from classes.Library import Library
from classes.Employee import Employee
from classes.Book import Book
from classes.Order import Order

library1 = Library('Jankowice', 'Żubrów 14', '43-215', '10-15', '875234123')

library2 = Library('Gliwice', 'Akademicka 3', '44-100', '8-16', '875234123')

book1 = Book(library1, datetime.date(2000, 1, 9), 'John', 'Doe', 450)
book2 = Book(library1, datetime.date(2005, 12, 29), 'John', 'Doe', 567)
book3 = Book(library1, datetime.date(2019, 10, 16), 'John1', 'Doe1', 100)
book4 = Book(library2, datetime.date(1996, 1, 1), 'John2', 'Doe2', 86)
book5 = Book(library2, datetime.date(1970, 5, 10), 'John3', 'Doe3', 764)


student1 = s.Student('Ala', 78)
student2 = s.Student('Franek', 45)
student3 = s.Student('Franek2', 45)


empl1 = Employee('Andrew', 'Gilding', datetime.date(2010, 9, 18),
                 datetime.date(1990, 3, 5), 'Radostowice',
                 'Kościelna 4', '22-918', '8879213123')
empl2 = Employee('Luke', 'Woodhouse', datetime.date(2010, 9, 18),
                 datetime.date(1990, 3, 5), 'Radostowice',
                 'Kościelna 4', '22-918', '8879213123')
empl3 = Employee('Jan', 'Kowalski', datetime.date(2010, 9, 18),
                 datetime.date(1990, 3, 5), 'Radostowice',
                 'Kościelna 4', '22-918', '8879213123')

order1 = Order(empl1, student1, [book2, book3, book4],
               datetime.date(2025, 5, 1))

order2 = Order(empl2, student2, [book1, book3, book5],
               datetime.date(2025, 5, 1))

print(str([book2]))

print(order1)
print(order2)
