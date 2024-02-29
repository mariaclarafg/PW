user_entry = input("Type a list of names separated by a space: ")

names = user_entry.split()

upper_names = list(map(str.upper, names))


print("Original list:", names)
print("List with the uppercase names:", upper_names)