# public protected private
class Worker:

    def __init__(self, name: str, age: float, salary: int):
        self.__name = name
        if age >= 80 or age < 18:
            self.__age = 35
        else:
            self.__age = age
        self.__salary = salary

    def print_my_info(self):
        print(self.__name, self.__salary)

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        # if isinstance(name, str):
        if type(name) is str:
            self.__name = name
        else:
            self.__name = "QWERTY"

    def get_age(self):
        return self.__age

    def set_age(self, age: float):
        if age >= 80 or age < 18:
            self.__age = 35
        else:
            self.__age = age


class Person(Worker):

    def __init__(self):
        super().__init__("Person", 36, 400)

    def print_me(self):
        print(self.__name)


worker_1 = Worker("Alex", 40, 10000)

list_of_names = []
list_of_names.append(worker_1.get_name())
print(list_of_names)
print(worker_1.get_age())
worker_1.set_age(50)
print(worker_1.get_age())

worker_1.set_name(123213213)

print(worker_1.get_name())

person = Person()
# person.print_me() # AttributeError: 'Person' object has no attribute '_Person__name'
