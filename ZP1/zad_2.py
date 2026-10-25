import datetime

class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Imię: {self.name}'


class Library:
    def __init__ (self,city:str, street:str, zip_zode:str, hours:str, phone:str):
        self.city = city
        self.street = street
        self.zip_code = zip_zode
        self.open_hours = hours
        self.phone = phone
    
    def __str__(self):
        return f'Adres bibliteki: {self.street}, {self.zip_code} {self.city}\nGodziny otwarcia {self.open_hours}\nTelefon:{self.phone}'
        pass
class Employee:

    def __init__ (self, first_n, last_n, hire_d:datetime.date, birth_d:datetime.date, city, street, zip_code, phone):
        self.first_name = first_n
        self.last_name = last_n
        self.hire_date = hire_d
        self.birth_date = birth_d
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    
    def __str__(self):
        return f'Imie: {self.first_name}, \nNazwisko: {self.last_name}, \nData zatrudenienia: {self.hire_date}, \nData urodzenia: {self.birth_date}, \nTelefon: {self.phone}\nAdres: {self.street}, {self.zip_code} {self.city}'
class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date  =  publication_date
        self.author_name  =author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    pass

    def __str__(self):
        return f'Biblioteka: {self.library} \nData publikacji: {self.publication_date} \nImię autora: {self.author_name} \nNazwisko autora: {self.author_surname} \nLiczba stron: {self.number_of_pages}'
        

class Order:
    def __init__(self, emplyee:Employee, student: Student, books: list, order_date ):
        self.employee = emplyee
        self.student = student
        self.books = books
        self.order_date = order_date
    pass

    def __str__(self):
        return f'Bibliotekarz: \n{self.employee}, \nStudent: \n{self.student}, \nData: {self.order_date}, \nKsiążki: {self.books}'
    


library1 = Library('Jankowice', 'Żubrów 14', '43-215', '10-15', '875234123')

library2 = Library('Gliwice', 'Akademicka 3', '44-100', '8-16', '875234123')

book1  = Book(library1, datetime.date(2000, 1, 9), 'John', 'Doe', 450)
book2 = Book(library1, datetime.date(2005, 12, 29), 'John', 'Doe', 567)
book3 = Book(library1, datetime.date(2019, 10, 16), 'John1', 'Doe1', 100)
book4 = Book(library2, datetime.date(1996, 1, 1), 'John2', 'Doe2', 86)
book5 = Book(library2, datetime.date(1970, 5, 10), 'John3', 'Doe3', 764)


student1 = Student('Ala', 78)
student2 = Student('Franek', 45)
student3 = Student('Franek2', 45)


empl1 = Employee('Andrew', 'Gilding', datetime.date(2010,9,18), datetime.date(1990,3,5), 'Radostowice', 'Kościelna 4', '22-918', '8879213123' )
empl2 = Employee('Luke', 'Woodhouse', datetime.date(2010,9,18), datetime.date(1990,3,5), 'Radostowice', 'Kościelna 4', '22-918', '8879213123' )
empl3 = Employee('Jan', 'Kowalski', datetime.date(2010,9,18), datetime.date(1990,3,5), 'Radostowice', 'Kościelna 4', '22-918', '8879213123' )

order1 = Order(empl1, student1, [book2, book3, book4], datetime.date(2025,5,1))

order2 = Order(empl2, student2, [book1, book3, book5], datetime.date(2025,5,1))

print(book2)

print(order2)