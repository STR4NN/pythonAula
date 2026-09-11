valor = (input("Digite um valor de no minimo 4 digitos para ser invertido: "))
numero = [valor]

primeiroNumero = numero[0][0]
segundoNumero = numero[0][1]
terceiroNumero = numero[0][2]
quartoNumero = numero[0][3]

numeroInverter = quartoNumero + terceiroNumero + segundoNumero + primeiroNumero

castingNumber = int(numeroInverter)
print("Numero invertido via lógica: ", castingNumber, type(castingNumber))


valor_invertido_funcao = str(valor)[::-1]
# Ou apenas
print("Valor invertido via função: ",valor_invertido_funcao, type(valor_invertido_funcao))

