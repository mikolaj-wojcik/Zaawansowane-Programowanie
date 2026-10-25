

def nalezy_do_zbioru(lista: list, num: int) -> bool:
    return num in lista


if nalezy_do_zbioru([8, 9, 10, 4, 1], 1):
    print('Zawiera się w liście')
else:
    print('Nie zawiera się w liście')
