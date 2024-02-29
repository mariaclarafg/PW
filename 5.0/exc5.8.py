user_entry = input("Type a list of numbers separated by a space: ")

numbers = list(map(float, user_entry.split()))

squared = list(map(lambda x: x**2, numbers))

print("Original list:", numbers)
print("Squared list:", squared)