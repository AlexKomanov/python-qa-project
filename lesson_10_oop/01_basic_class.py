class MyGlobalPerson:
    name = "Alex"
    age = 35
    is_working = True
    my_skills = ("Java", "Python", "TS")

    def print_my_name(self):
        print(self.name)
        print(id(self))

    def say_hello_to(self, greeting: str):
        print(f"{greeting}, {self.name}!")


my_person = MyGlobalPerson()
me = MyGlobalPerson()

print(my_person.name)
# my_person.name = "Dan"
# print(my_person.name)
print(my_person.my_skills)
my_person.print_my_name()
my_person.say_hello_to("Hello")

me.name = "Alexander"
me.say_hello_to("Good Morning")

me.print_my_name()
my_person.print_my_name()
