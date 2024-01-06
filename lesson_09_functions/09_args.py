num_1 = 5
num_2 = 10

my_tuple = (4, 6, 7)
my_tuple_2 = (4, True, "text")
my_list = [4, 6, 7, 10, 60]


def sum_first_last_numbers(*numbers: int):
    print(type(numbers))
    print("length = ", len(numbers))
    print(numbers[0] + numbers[-1])


sum_first_last_numbers(num_1, num_2, 3, 6, 7)
sum_first_last_numbers(3, 6, 7)
sum_first_last_numbers(3)

