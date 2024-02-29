soma_primos = 0

for num in range(2, 101):
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        soma_primos += num

print(f"A soma dos números primos de 1 a 100 é: {soma_primos}")