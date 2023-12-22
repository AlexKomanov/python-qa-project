numb_1 = int(input("First number: "))
numb_2 = float(input("Second number: "))


def sum_two_numbers(number_1: int, number_2: float):
    return number_1 + number_2


# def sum_two_numbers(number_1: int, number_2: float):
#     if numb_1 > 5:
#         return number_1 + number_2
#     else:
#         return


def increase_number(number: float):
    print(number + 5)


result_from_number = sum_two_numbers(numb_1, numb_2)
increase_number(result_from_number)
