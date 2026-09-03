# Tudo o que vem do terminal é STRING.
# Mesmo sendo números.

nome = input("Digite o seu nome: ")
print(nome, type(nome))

idade = int(input("Digite sua idade: "))
print(idade, type(idade))

# Funções de conversão de dados.

# int = int()
# float = float()
# boolean = bool()

altura = float(input("Digite sua altura: "))
print(altura, type(altura))


# No boolean, é esperado 1 para true e 0 para false.
situacao = bool(int(input("Digite 0 para sair ou 1 para entrar: ")))
print(situacao, type(situacao))

