original_list = [5, 10, 15, 20, 25, 30]

# def filter_list(list_elem: int):
#     return list_elem >= 20
# new_filtered_list = list(filter(filter_list, original_list))

new_filtered_list = list(filter(lambda x: x >= 20, original_list))

print(new_filtered_list)
