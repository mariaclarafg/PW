#Use list comprehension para criar uma lista com os números divisíveis por 3 ou 5 de 0 a 30.

numbers = list(range (0, 31))

list = [x for x in numbers if x % 3 == 0 or x % 5 == 0]
print(list) 