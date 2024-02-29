maior_numero = float('-inf')  
menor_numero = float('inf')   

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print(f"O maior número digitado é: {maior_numero}")
print(f"O menor número digitado é: {menor_numero}")