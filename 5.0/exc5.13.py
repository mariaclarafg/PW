users_list1 = input("Type a list of numbers separated by a space: ")

users_list2 = input("Type a list of numbers separated by a space: ")

list1 = [float(number) for number in users_list1.split()]
list2 = [float(number) for number in users_list2.split()]

if len(list1) != len(list2):
    print("Both lists have to be the same lenth.")
else:
    average = [(value1 + value2) / 2 for value1, value2 in zip(list1, list2)]

    print("First list:", list1)
    print("Secund list:", list2)
    print("Average:", average)