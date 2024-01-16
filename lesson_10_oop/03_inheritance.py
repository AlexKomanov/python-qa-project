import random


class General:
    def __init__(self):
        pass

    def random_number(self):
        return random.randrange(1, 100)


class Vehicle:

    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year

    def move(self):
        print(f"{self.model} is moving!")

    def who_am_i(self):
        print("I'm a general vehicle")


class Car(Vehicle, General):  # class Car extends Vehicle
    def __init__(self, car_model: str, car_year: int, is_electrical: bool):
        super().__init__(car_model, car_year)
        self.is_electrical = is_electrical

    def who_am_i(self):
        print(f"I'm a car of model {self.model}")

    print_my_info = lambda self: print(f"lambda {self.model}")


class BMW(Car):

    def __init__(self, car_model: str, car_year: int, is_electrical: bool, series: int):
        super().__init__(car_model, car_year, is_electrical)
        self.series = series

    def who_am_i(self):
        print("I'm BMW car")


my_vehicle = Vehicle("Vehicle", 2024)

print(my_vehicle.year)
print(my_vehicle.model)
my_vehicle.move()
my_vehicle.who_am_i()

my_car = Car("Tesla", 2019, True)

print(my_car.year)
print(my_car.model)
print(my_car.is_electrical)
my_car.move()
my_car.who_am_i()
my_car.print_my_info()

bmw = BMW("BMW", 2025, True, 6)

print(bmw.series)
print(bmw.random_number())
