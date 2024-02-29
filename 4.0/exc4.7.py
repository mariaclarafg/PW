nome_usuario = input("Digite um nome de usuário: ")

nome_usuario_limpo = ''.join(c for c in nome_usuario if c.isalnum())

print(f"Nome de usuário original: {nome_usuario}")
print(f"Nome de usuário limpo: {nome_usuario_limpo}")

senha = input("Digite uma senha: ")

senha_limpa = ''.join(c for c in senha if c.isalnum())

print(f"Senha original: {senha}")
print(f"Senha limpa: {senha_limpa}")