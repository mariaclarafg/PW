frase = input("Digite uma frase: ")
palavra_existente = input("Digite uma palavra presente na frase: ")
palavra_ausente = input("Digite uma palavra ausente na frase: ")

frase_modificada = frase.replace(palavra_existente, palavra_ausente)

print("Frase original:", frase)
print("Frase modificada:", frase_modificada)