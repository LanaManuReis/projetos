#Entrada - o programa solicitará as informações.
valortotal = float(input('Digite o valor total da compra: '))

#Processamento - programa irá calcular o desconto com base no valor total.
if valortotal < 200:
  desconto = valortotal * 0.05
elif valortotal >= 200  and valortotal < 300:
  desconto = valortotal * 0.1
else:
  desconto = valortotal * 0.15

valorapagar = valortotal - desconto
# Saída - o programa irá exibir o valor do desconto e o total a pagar.
print(f'Valor do desconto: R$ {desconto:.2f}')
print(f'Valor a pagar: R$ {valorapagar:.2f}')