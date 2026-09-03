nome = input(" Qual seu nome ? ")
idade = int(input("Digite sua idade: "))

# print (type(nome))
# print (type(idade))

print("Eu sou o " + nome + " e tenho " + str(idade) + " anos.")


if(nome == "Gustavo"):
    print("\nVocê é meu chará!")
elif(idade == 18):
    print("Nossa! Temos a mesma idade!")

else:
    print("Legal!")