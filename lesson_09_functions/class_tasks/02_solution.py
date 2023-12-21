list_of_names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
print("unfiltered list:", list_of_names)

# Get only names where a length higher than 4
filtered_list = list(filter(lambda x: len(x) > 4, list_of_names))
print("filtered_list:", filtered_list)
