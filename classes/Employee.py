import datetime
from classes import Student as s
class Employee:

    def __init__(self, first_n, last_n, hire_d: datetime.date,
                 birth_d: datetime.date, city, street,
                 zip_code, phone):
        self._first_name = first_n
        self._last_name = last_n
        self._hire_date = hire_d
        self._birth_date = birth_d
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def hire_date(self) -> datetime.date:
        return self._hire_date

    @property
    def birth_date(self) -> datetime.date:  
        return self._birth_date

    @property
    def city(self) -> str:
        return self._city

    @property
    def street(self) -> str:
        return self._street

    @property
    def zip_code(self) -> str:
        return self._zip_code

    @property
    def phone(self) -> str:
        return self._phone

    def __str__(self):
        return f''' Imie: {self.first_name},
                    Nazwisko: {self.last_name},
                    Data zatrudenienia: {self.hire_date},
                    Data urodzenia: {self.birth_date},
                    Telefon: {self.phone}
                    Adres: {self.street}, {self.zip_code} {self.city}'''