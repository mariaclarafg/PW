temperatura = float(input("Digite a temperatura em graus Celsius: "))


faixa_normal_inferior = 36
faixa_normal_superior = 37

if temperatura < faixa_normal_inferior:
    print("A temperatura está abaixo da faixa normal.")
elif temperatura > faixa_normal_superior:
    print("A temperatura está acima da faixa normal.")
else:
    print("A temperatura está dentro da faixa normal.")
