
from classes import Library


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages
    pass

    @property
    def library(self) -> Library:
        return self._library
    @property
    def publication_date(self) -> datetime.date:
        return self._publication_date
    @property
    def author_name(self) -> str:
        return self._author_name
    @property
    def author_surname(self) -> str:
        return self._author_surname
    @property
    def number_of_pages(self) -> int:       
        return self._number_of_pages    
    def __str__(self):
        return f''' Biblioteka: {self.library}
                    Data publikacji: {self.publication_date}
                    Imię autora: {self.author_name}
                    Nazwisko autora: {self.author_surname}
                    Liczba stron: {self.number_of_pages}'''

