# Custo final do carro para consumidor

custo_fabrica = float(input("Digite o valor do carro:  "))

percentual_distribuidor = 0.28
percentual_impostos = 0.45

custo_distribuidor = custo_fabrica * percentual_distribuidor
custo_impostos = custo_fabrica * percentual_impostos

custo_final = custo_fabrica + custo_distribuidor + custo_impostos/100

print("O custo final do carro para o consumidor é R$:  ", custo_final)

