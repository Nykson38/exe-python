altura_str = input("Digite a sua altura em metros (ex: 1.75): ").replace(',', '.')
h = float(altura_str)
#.replece procura vírgulas e troca-as por pontos.

sexo = input("Digite o seu sexo (M para homem, F para mulher): ").strip().upper()
#.upper Converte todas as letras do texto para maiúsculas.

if sexo == 'M':
    peso_ideal = (72.7 * h) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * h) - 44.7
else:
    peso_ideal = None

if peso_ideal is not None:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Opção de sexo inválida. Por favor, digite M ou F.")