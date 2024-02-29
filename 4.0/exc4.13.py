frase = input("Digite uma frase: ")

palavras = frase.split()

palavras_sem_espacos = [palavra.strip() for palavra in palavras]

frase_sem_espacos = ' '.join(palavras_sem_espacos)

print("Frase sem espaços em branco desnecessários:", frase_sem_espacos)