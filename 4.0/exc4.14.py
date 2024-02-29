frase = input("Digite uma frase: ")

palavras = frase.split()

print("Posição inicial de cada palavra:")
for i, palavra in enumerate(palavras, start=1):
    print(f"A palavra '{palavra}' começa na posição {i}")