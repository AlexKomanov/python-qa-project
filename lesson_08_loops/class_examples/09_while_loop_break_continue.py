counter = 1

while counter <= 20:
    # counter += 1
    if counter == 7:
        counter += 1
        continue
    if counter == 11:
        # pass
        print(counter)
        break
    print(counter)
    counter += 1
else:
    print("Loop was finished")

print("After while")
