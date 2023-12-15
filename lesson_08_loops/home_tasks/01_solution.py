list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

# iterate reversed list
new_list_2 = list1[::-1]
for item in new_list_2:
    print(item)
