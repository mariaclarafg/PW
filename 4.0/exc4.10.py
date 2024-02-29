frase = input("Digite uma frase: ")

artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']

palavras = frase.split()
frase_sem_artigos = ' '.join(palavra for palavra in palavras if palavra.lower() not in artigos)

print("Frase sem artigos:", frase_sem_artigos)