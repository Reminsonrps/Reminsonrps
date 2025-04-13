# Solicita ao usuário a quantidade de quilômetros percorridos e a quantidade de dias de aluguel
km_percorridos = float(input("Quantos km você percorreu com o carro alugado? "))
dias_alugados = int(input("Por quantos dias você alugou o carro? "))

# Define os valores de cobrança
preco_por_dia = 60.0
preco_por_km = 0.15

# Calcula o custo total
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

# Exibe o valor a pagar
print(f"O total a pagar pelo aluguel do carro é: R${custo_total:.2f}")