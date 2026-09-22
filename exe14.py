ncont = input("Qual o numero da conta :")
saldo = float(input("Digite seu saldo :"))
debito = float(input("Valor em débito :"))
credito = float(input("Valor em crédito :"))

saldoatual = saldo - debito + credito 

print(f"Seu saldo atual é {saldoatual}")

if saldoatual >= 0:
    print("Seu saldo está positivo")

else: 
    print("Seu saldo é negativo")