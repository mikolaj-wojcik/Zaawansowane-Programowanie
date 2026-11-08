from classes import Employee
from classes import Student as s


class Order:
    def __init__(self, emplyee: Employee, student: s.Student,
                 books: list, order_date):
        self.employee = emplyee
        self.student = student
        self.books = books
        self.order_date = order_date
    pass

    def __str__(self):
        return f'''Bibliotekarz: \n{self.employee}, \n
        Student: \n{self.student}, \nData: {self.order_date}, \nKsiążki:
        {[str(book) for book in self.books]}'''
