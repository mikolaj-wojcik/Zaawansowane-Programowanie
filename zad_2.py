
def mulitplicate_list_for(numbers):
    ret_list = []
    for number in numbers:
        ret_list.append(number * 2)

    return ret_list


def multiplicate_list_computed(numbers):
    ret_list = [number * 2 for number in numbers]

    return ret_list


print(mulitplicate_list_for([14, 18.6, 453.099, 12.7777]))
print(multiplicate_list_computed([14, 18.6, 453.099, 12.7777]))
