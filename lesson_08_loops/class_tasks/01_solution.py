number_start = int(input("Enter a first number: "))
number_end = int(input(" Enter a second number: "))

for i in range(number_start, number_end + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
