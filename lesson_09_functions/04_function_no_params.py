import datetime
import random


def get_today_date():
    return datetime.datetime.today()


def get_random_number(number: int):
    return random.randint(1, number)


print(get_today_date())
print(get_random_number(10))
