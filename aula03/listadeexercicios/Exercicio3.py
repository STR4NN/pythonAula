print("Bem vindo a calculadora de IMC!")

print("Para podermos te classificar digite esses dois valores!")

print("---------------------------------")


peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("------------------------------")
print("\nSeu imc é de: ", imc)