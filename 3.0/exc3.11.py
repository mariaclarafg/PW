soma = 0

for numero in range(1, 101):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero

print(f"A soma dos números divisíveis por 3 ou 5 de 1 a 100 é: {soma}")