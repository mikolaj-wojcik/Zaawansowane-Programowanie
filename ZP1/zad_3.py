def dziesiec_liczb_co_druga(numbers):
    for i in range(len(numbers)):
        if i % 2 == 1:
            print(numbers[i])

    pass


dziesiec_liczb_co_druga([10, 31, 12, 3, 444.2, 24235.4, 12, 99, 14, 76])
