satual = float(input("Digite o seu salario atual :"))

if satual <= 280:
    percentual = 20 

elif satual <= 700:
    percentual = 15

elif satual <= 1500:
    percentual = 10

else:
    percentual = 5 

valmento = satual * (percentual / 100)
nsalario = satual + valmento

print(f"Salario antes do reajuste: R$ {satual}")
print(f"Percentual de aumento aplicado: {percentual}% ")
print(f"Valor do aumento: R$ {valmento:.2f}")
print(f"Salario após o aumento: R$ {nsalario:.2f}")
