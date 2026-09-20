#Entrada, o usuário fornecerá os dados
tipo_imovel = input('Digite o tipo do seu imóvel(comercial, casa ou apartamento): ')
consumo = float(input('Digite o consumo mensal de água em m³: '))

#Processamento, o programa vai analisar as informações
if tipo_imovel == 'comercial':
    mensagem = 'Tarifa comercial aplicada - consulte o plano corporativo.'

elif tipo_imovel == 'apartamento' and consumo < 10: 
    mensagem = 'Consumo econômico - excelente controle de água!'

elif tipo_imovel == 'apartamento' or tipo_imovel == 'casa' and consumo <= 25: 
    mensagem = 'Consumo moderado – dentro do padrão residencial.'

else:
    mensagem = 'Consumo excessivo - adote medidas de economia e verifique vazamentos.'
    

#Saída
print(mensagem)
