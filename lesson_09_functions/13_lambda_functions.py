say_hello = lambda: print("Hello World")

say_hello()

sum_of_numbers = lambda num_1, num_2: print(num_1 + num_2)

sum_of_numbers(5, 10)

# def sum_of_numbers(num_1, num_2):
#     return num_1 + num_2

sum_of_numbers = lambda num_1, num_2: num_1 + num_2

result = sum_of_numbers(10, 20)
print(result)
