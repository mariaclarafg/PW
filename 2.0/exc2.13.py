idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (f para feminino, m para masculino): ")

if (genero == "f" and idade >= 60) or (genero == "m" and idade >= 65):
    print("Você é elegível para aposentadoria.")
else:
    print("Você não é elegível para aposentadoria.")