nome = input("Digite seu nome :")
idade = int(input("Digite a sua idade :"))

if(idade >= 0 and idade <= 2):
    print(f"{nome} está com {idade} e pela tabela é considerado uma bebe")


elif(idade >= 3 and idade <= 11):
    print(f"{nome} está com {idade} e pela tabela é considerado uma criança")


elif(idade >= 12 and idade <= 21):
    print(f"{nome} está com {idade} e pela tabela é considerado uma jovem")


elif(idade >= 22 and idade <= 64):
    print(f"{nome} está com {idade} e pela tabela é considerado uma adulto")


elif(idade >= 65 and idade <= 100):
    print(f"{nome} está com {idade} e pela tabela é considerado uma idoso")


elif(idade >= 101 ):
    print(f"{nome} está com {idade} e pela tabela é considerado uma muito velhinho")


