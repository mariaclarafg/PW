list_numbers = input("Type a list of numbers separated by a space: ")

numbers = [float(number) for number in list_numbers.split()]

inverted_numbers = numbers[::-2]

print("Original list:", numbers)
print("Inverted elements with even indexes:", inverted_numbers)