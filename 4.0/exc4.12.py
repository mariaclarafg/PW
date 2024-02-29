frase = input("Digite uma frase: ")

palavras = frase.split()

contador_palavras_o = 0
contador_palavras_a = 0

for palavra in palavras:
    if palavra.endswith('o'):
        contador_palavras_o += 1
    elif palavra.endswith('a'):
        contador_palavras_a += 1

print(f"Quantidade de palavras terminando em 'o': {contador_palavras_o}")
print(f"Quantidade de palavras terminando em 'a': {contador_palavras_a}")