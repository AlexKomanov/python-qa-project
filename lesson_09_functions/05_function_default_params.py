import random


def get_random_number(start_number: int, number: int = 1000000):
    return random.randint(start_number, number)


print(get_random_number(1))
print(get_random_number(1, 10))
