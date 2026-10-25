

def is_even(a) -> bool:
    return a % 2 == 0


jest_parzysta = is_even(987)

if jest_parzysta:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')
