class Library:
    def __init__(self, city: str, street: str, zip_zode: str, hours: str,
                 phone: str):
        self._city = city
        self._street = street
        self._zip = zip_zode
        self._open_hours = hours
        self._phone = phone

    def __str__(self):
        return f'''Adres bibliteki: {self.street}, {self.zip} {self.city}
Godziny otwarcia {self.open_hours}\nTelefon:{self.phone}'''
        pass

    @property
    def city(self) -> str:
        return self._city

    @property
    def street(self) -> str:
        return self._street

    @property
    def zip(self) -> str:
        return self._zip

    @property
    def open_hours(self) -> str:
        return self._open_hours 

    @property
    def phone(self) -> str:
        return self._phone
