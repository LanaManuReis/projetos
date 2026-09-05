# Entrada
nome = input('Digite o nome do aparelho: ')
potencia = float(input('Digite a potência: '))
horasDia = float(input('digite as horas/dias: '))

# Processamento/Cálculo
consumoMensal = potencia * horasDia * 30 / 1000
custoMensal = consumoMensal * 0.75

#Saída 
print(f'Aparelho: {nome}')
print(f'Consumo estimado: {consumoMensal:.0f} kWh/mês')
print(f'Custo mensal estimado: R$ {custoMensal:.2f}')