nome = 'Mirelle Mota'
peso = 56.0
altura = 1.56
imc = peso / (altura * altura)

#f-strings = formatação

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1, linha_2, linha_3)

