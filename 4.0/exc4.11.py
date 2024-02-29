frase = input("Digite uma frase: ")

tamanho_substr = 6
substrings = [frase[i:i+tamanho_substr] for i in range(0, len(frase), tamanho_substr)]

print("Substrings de 6 caracteres:")
for substr in substrings:
    print(substr)