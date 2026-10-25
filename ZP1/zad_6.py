

def polacz_listy(lista1: list, lista2: list) -> list:
    lista = lista1 + lista2
    lista = list(set(lista))

    lista_pow = [elem ** 3 for elem in lista]
    return lista_pow


print(polacz_listy([33, 55, 1], [4, 3, 1]))
