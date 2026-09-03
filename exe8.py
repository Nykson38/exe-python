distancia = float(input("Qual a distancia da viagem?"))
consumo = float(input("Qual o consumo do veiculo?"))
combustivel = float(input("Qual o preço do combustivel?"))

litros = distancia / consumo
total = litros * combustivel

print(f"O custo estimado é  : {total}")
print(f"Litros necessarios : {litros}")