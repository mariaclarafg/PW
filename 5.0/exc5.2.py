#Use list comprehension para criar uma lista com as palavras que contêm a letra “a” em uma frase digitada pelo usuário, substituindo a letra por “o”. 

phrase = input("Type a phrase: ")


list = [word.replace('a', 'o') for word in phrase.split() if 'a' in word]

print(list)
