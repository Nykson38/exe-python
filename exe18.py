vhora = float(input("Digite o valor da sua hora :"))
htrabalhadas = float(input("Digite quantas horas você trabalhou no mês"))

sbruto = vhora * htrabalhadas

if sbruto <= 900:
    percentual = 0

elif sbruto <= 1500:
    percentual = 5

elif sbruto <= 2500:
    percentual = 10

else:
    percentual = 20

desconto_ir = sbruto * (percentual / 100)
desconto_inss = sbruto * 0.10
desconto_sindicato = sbruto * 0.03
fgts = sbruto * 0.11

total_d = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = sbruto - total_d

texto_ir = "Isento" if percentual == 0 else f"{percentual}%"

print(f"Salário bruto: ({vhora:.0f} * {htrabalhadas:.0f}) :R$ {sbruto:8.2f}")

print(f"(-) IR ({texto_ir})                    : R$ {desconto_ir:8.2f}")

print(f"(-) INSS (10%)                 : R$ {desconto_inss:8.2f}")

print(f"(-) Sindicato (3%)             : R$ {desconto_sindicato:8.2f}")

print(f"FGTS (11%)                     : R$ {fgts:8.2f}")

print(f"Total de descontos             : R$ {total_d:8.2f}")

print(f"Salário Liquido                : R$ {salario_liquido:8.2f}")