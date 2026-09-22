qtd_pequenas = int(input("Digite a quantidade de camisetas PEQUENAS: "))
qtd_medias = int(input("Digite a quantidade de camisetas MÉDIAS: "))
qtd_grandes = int(input("Digite a quantidade de camisetas GRANDES: "))


preco_pequena = 10.00
preco_media = 12.00
preco_grande = 15.00


total_pequenas = qtd_pequenas * preco_pequena
total_medias = qtd_medias * preco_media
total_grandes = qtd_grandes * preco_grande

valor_total = total_pequenas + total_medias + total_grandes


print("\n--- RESUMO DA VENDA ---")
print(f"Camisetas Pequenas ({qtd_pequenas}x): R$ {total_pequenas:.2f}")
print(f"Camisetas Médias   ({qtd_medias}x): R$ {total_medias:.2f}")
print(f"Camisetas Grandes  ({qtd_grandes}x): R$ {total_grandes:.2f}")
print("-" * 30)
print(f"Valor Total da Compra: R$ {valor_total:.2f}")