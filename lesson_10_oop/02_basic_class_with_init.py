class MyGlobalPerson:
    name = "General Name"
    age = 35
    is_working = True
    my_skills = ("Java", "Python", "TS")

    def __init__(self, name: str = "Name", age: int = 35):
        self.name = name
        if age >= 18:
            self.age = age
        else:
            self.age = 18

    def print_my_name(self):
        print(self.name)
        # print(id(self))

    def say_hello_to(self, greeting: str):
        print(f"{greeting}, {self.name}!")


# print(MyGlobalPerson.age)
# print(MyGlobalPerson.my_skills)
# print(MyGlobalPerson.name)

my_person = MyGlobalPerson("Alex", 35)
me = MyGlobalPerson(age=40)
print(my_person.name)
print(my_person.age)
print(me.name)
print(me.age)
#
# my_person.print_my_name()
# me.print_my_name()
