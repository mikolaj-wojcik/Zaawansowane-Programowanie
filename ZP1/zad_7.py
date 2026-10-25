import requests

BREWERY_API = 'https://api.openbrewerydb.org/v1/breweries'


class Brewery:

    def __init__(self, id, name, type, a1, a2, a3,
                 city, state_province, postal, country,
                 longtitude, latitude, phone, url, state, street):
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = type
        self.address_1: str = a1
        self.address_2: str = a2
        self.address_3: str = a3
        self.city: str = city
        self.state_province: str = state_province
        self.postal_code: str = postal
        self.country: str = country
        self.longtitude: float = longtitude
        self.latitude: float = latitude
        self.phone: str = phone
        self.website_url: str = url
        self.state: str = state
        self.street: str = street
        pass

    def __str__(self):
        return f'''Brewery: {self.name}
Type: {self.brewery_type},
Address 1: {self.address_1},
Address 2: {self.address_2},
Address 3: {self.address_3},
City: {self.city},
State/Province: {self.state_province},
Postal Code: {self.postal_code},
Country: {self.country},
Longitude: {self.longtitude},
Latitude: {self.latitude},
Phone: {self.phone},
Website URL: {self.website_url},
State: {self.state},
Street: {self.street}'''


def listbreweries() -> list:
    resp = requests.get(BREWERY_API + '?per_page=20')
    brew_list = []
    if resp.status_code == 200:
        resp_json = resp.json()

        for single in resp_json:
            brew_list.append(Brewery(single['id'], single['name'],
                                     single['brewery_type'],
                                     single['address_1'],
                                     single['address_2'],
                                     single['address_3'], single['city'],
                                     single['state_province'],
                                     single['postal_code'],
                                     single['country'],
                                     single['longitude'],
                                     single['latitude'], single['phone'],
                                     single['website_url'],
                                     single['state'],
                                     single['street']))
    return brew_list


list_of_breweries = listbreweries()

for brewery in list_of_breweries:
    print(brewery)
