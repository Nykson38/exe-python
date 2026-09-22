qtd_sanduiches = int(input("Digite a quantidade de sanduíches a fazer: "))

peso_queijo_kg = (qtd_sanduiches * 2 * 50) / 1000
peso_presunto_kg = (qtd_sanduiches * 1 * 50) / 1000
peso_carne_kg = (qtd_sanduiches * 1 * 100) / 1000


print("\n--- QUANTIDADE DE INGREDIENTES PARA COMPRA ---")
print(f"Queijo:   {peso_queijo_kg:.2f} kg")
print(f"Presunto: {peso_presunto_kg:.2f} kg")
print(f"Carne:    {peso_carne_kg:.2f} kg")