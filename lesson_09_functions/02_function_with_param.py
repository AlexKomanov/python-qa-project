def say_hello(name: str):
    print(f"Good Evening {name.lower()}!")


say_hello("Shalom")
say_hello("Alex")
say_hello("Inbar")
say_hello("תגגכגכגכ")
say_hello("123456")
# say_hello("123456", "Alex") # TypeError: say_hello() takes 1 positional argument but 2 were given

# say_hello() # TypeError: say_hello() missing 1 required positional argument: 'name'
# say_hello(555)
