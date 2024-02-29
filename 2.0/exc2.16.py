#Escreva um programa que pergunte ao usuário seu gênero (M para masculino, F
#para feminino) e exiba uma mensagem de “Gênero masculino” ou “Gênero feminino”.

genero = input("Digite seu gênero (M para masculino, F para feminino): ")

if genero == "M":
    print("Gênero masculino.")
elif genero == "F":
    print("Gênero feminino.")
else:
    print("Gênero não reconhecido.")