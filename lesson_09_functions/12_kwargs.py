my_details = {
    "name": "Alex",
    "age": 35,
    "is_soldier": False,
    "address": {
        "city": "Karmiel",
        "index": 345678,
        "name": "CRM"
    },

}


def print_dictionary_pairs(**pairs):
    # print(type(pairs))
    print("list:", list(pairs.items()))
    print("list_of_keys:", list(pairs.keys()))
    print("list_of_values():", list(pairs.values()))
    print(pairs)
    for item in pairs.items():
        print(item)
    for k, v in pairs.items():
        print(f"{k} - {v}")


# print(**kwargs)
# end= _________
# sep= _________

print_dictionary_pairs(city="Karmiel", age=35, name="Alex")

