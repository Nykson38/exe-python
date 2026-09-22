TOTAL_ALUNOS = 50

qtd_feminino_altas = 0  

total_masculino = 0      

masculino_status_bom = 0 

print("=== CADASTRO DE DADOS DE EDUCAÇÃO FÍSICA ===")

for i in range(1, TOTAL_ALUNOS + 1):
    print(f"\n--- Aluno {i} de {TOTAL_ALUNOS} ---")
    
    matricula = input("Matrícula: ")
    sexo = input("Sexo (M/F): ").strip().upper()
    altura = float(input("Altura (em cm): "))
    status_fisico = int(input("Status físico (1-bom, 2-regular, 3-ruim): "))
    
    
    if sexo == 'F' and altura > 170:
        qtd_feminino_altas += 1
        
   
    if sexo == 'M':
        total_masculino += 1
        if status_fisico == 1:
            masculino_status_bom += 1


if total_masculino > 0:
    pct_masculino_bom = (masculino_status_bom / total_masculino) * 100
else:
    pct_masculino_bom = 0.0


print("\n" + "=" * 40)
print("=== RESULTADOS DA ANÁLISE ===")
print("=" * 40)
print(f"a) Quantidade de alunas (F) com altura > 170 cm: {qtd_feminino_altas}")

if total_masculino > 0:
    print(f"b) Porcentagem de alunos masculinos com status 'bom': {pct_masculino_bom:.2f}%")
else:
    print("b) Nenhum aluno do sexo masculino foi informado.")