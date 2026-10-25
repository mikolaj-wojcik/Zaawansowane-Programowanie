def dziesiec_liczb_parz(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            print(numbers[i])

    pass


dziesiec_liczb_parz([10, 31, 12, 3, 444.2, 24235.4, 18.98, 99, 14, 76])
