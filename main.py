horas_trabalhadas = 10
taxa_por_hora = 30  # Definindo uma taxa por hora

def freela_calculator(horas, taxa):
    total = horas * taxa
    print(f"Total de horas trabalhadas foi {horas}")
    print(f"Com a taxa de R${taxa} por hora, o pagamento total será R${total:.2f}")

freela_calculator(horas_trabalhadas, taxa_por_hora)