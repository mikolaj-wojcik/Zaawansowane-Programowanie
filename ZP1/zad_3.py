
class Property:
    def __init__(self, area, rooms: int, address):
        self.area = area
        self.rooms = rooms
        self.address = address

    def __str__(self):
        return f'''Powierzchnia: {self.area}\nPokoje: {self.rooms}
Adres: {self.address}'''
        pass


class House(Property):
    def __init__(self, area, rooms: int, address, plot: int):
        super().__init__(area, rooms, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f'\nDziałka: {self.plot}'


class Flat(Property):
    def __init__(self, area, rooms: int, address, floor: int):
        super().__init__(area, rooms, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f'\nPiętro: {self.floor}'


dom = House(342, 8, 'Wspólna 14', 14)
mieszkanie = Flat(34, 3, 'Wolska 2', 2)

print(f'Dom: {dom}')
print(f'Mieszkanie: {mieszkanie}')
