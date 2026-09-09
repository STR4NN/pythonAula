print("---------------Análise de Salário-------------------")

salarioBase = 1800

nomeVendedor = input("Digite o seu nome:  ")
quantidadeProdutosVendidos = int(input("Digite quantos produtos você venceu: "))

comissaoProduto = quantidadeProdutosVendidos * 150

valorTotalVendas = int(input("Valor total das suas vendas: "))
comissaoValorTotal = valorTotalVendas * 0.03

print(comissaoValorTotal)
print(comissaoProduto)

salarioFinal = salarioBase + comissaoProduto + comissaoValorTotal

print("O salario final do ", nomeVendedor, " é de : ", salarioFinal)
