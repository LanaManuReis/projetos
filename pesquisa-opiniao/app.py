# Pesquisa de opinião - TudoWeb

excelente = 0
ruim = 0

for i in range(50):
    nome = input('Digite seu nome')
    idade = int(input('Digite sua idade'))
    opiniao = int(input('Digite sua opinião (1-Excelente, 2-Bom, 3-Ruim )'))
    if opiniao == 1:
         excelente += 1
    elif opiniao == 3:
         ruim += 1

print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)