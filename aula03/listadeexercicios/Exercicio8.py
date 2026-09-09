print("-----------Consumo médio do seu veiculo-------------------")

distanciaPercorrida = int(input("Digite a distancia percorrida (em KM): "))
print("-----------------------------")
combustivelGasto = int(input("Digite o combustivel gasto (Em litros): "))

consumoMedio = distanciaPercorrida / combustivelGasto

print("\n Seu veiculo faz ", consumoMedio, " km por litro.")