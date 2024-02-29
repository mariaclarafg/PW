user_entry = input("Type a list of numbers separated by a space: ")


numbers = [int(number) for number in user_entry.split()]

even_numbers = [number for number in numbers if number % 2 == 0]

print("Original list:", numbers)
print("Even numbers:", even_numbers)