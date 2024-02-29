users_list = input("Type a list of numbers separated by a space: ")
number_reference = float(input("Type a referenced number: "))

numbers = [float(number) for number in users_list.split()]
higher_position = None

for i, number in enumerate(numbers):
    if number > number_reference:
        higher_position = i
        break


if higher_position is not None:
    print(f"The first element higher than {number_reference} is in the position {higher_position}.")
else:
    print(f"There is no element higher than {number_reference}.")