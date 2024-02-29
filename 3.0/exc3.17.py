maior_numero = float('-inf')  
segundo_maior_numero = float('-inf')
menor_numero = float('inf')  
segundo_menor_numero = float('inf')

for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))

    if numero > maior_numero:
        segundo_maior_numero = maior_numero
        maior_numero = numero
    elif numero > segundo_maior_numero and numero != maior_numero:
        segundo_maior_numero = numero

    if numero < menor_numero:
        segundo_menor_numero = menor_numero
        menor_numero = numero
    elif numero < segundo_menor_numero and numero != menor_numero:
        segundo_menor_numero = numero

print(f"O segundo maior número digitado é: {segundo_maior_numero}")
print(f"O segundo menor número digitado é: {segundo_menor_numero}")