import random


def get_random_number(start_number: int = 1, end_number: int = 100):
    return random.randint(start_number, end_number)


# print(get_random_number(end_number=500, start_number=15))
print(get_random_number(end_number=500))

print(get_random_number(100, 500))


def login(username: str = "user", password: str = "password", url: str = "localhost"):
    pass


login(url="new")
