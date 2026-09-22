vaquisicao = float(input("Digite o valor de aquisição do produto (R$): "))


if vaquisicao < 50.00:
    
    valor_venda = vaquisicao * 1.45
else:

    
    valor_venda = vaquisicao * 1.30


print(f"O valor de venda do produto é: R$ {valor_venda:.2f}")