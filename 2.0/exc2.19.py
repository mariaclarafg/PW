numeros = [int(input(f"Digite o {i + 1}º número inteiro: ")) for i in range(5)]

if all(numero % 2 == 0 for numero in numeros):
    print("Todos os números são pares.")
else:
    print("Pelo menos um número é ímpar.")