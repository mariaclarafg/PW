frase = input("Digite uma frase: ")

palavras = frase.split()

contagem_palavras = {}

for palavra in palavras:
    palavra = palavra.lower() 
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print("Contagem de cada palavra:")
for palavra, contagem in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece {contagem} vezes na frase.")