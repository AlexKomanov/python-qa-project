def count_args(*arguments):
    print("type is ", type(arguments))
    return len(arguments)


print(count_args(1, 2, 3))
print(count_args(1, 3))
print(count_args(1))
print(count_args())
