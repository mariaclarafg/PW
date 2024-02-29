#Use list comprehension para criar uma lista com o quadrado dos números pares entre 0 e 10.

numbers = list(range (0, 11))

squared = [x**2 for x in numbers if x % 2 == 0]
print(squared) 