num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite o número real: "))


calc1 = (2 * num_int1) * (num_int2 / 2)


calc2 = (3 * num_int1) + num_real


calc3 = num_real ** 3


print(f"Produto do dobro do primeiro com metade do segundo: {calc1}")
print(f"Soma do triplo do primeiro com o terceiro: {calc2}")
print(f"Terceiro elevado ao cubo: {calc3}")