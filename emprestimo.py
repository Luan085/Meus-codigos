# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa  deve perguntar
# o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode 
# ser superior a 30% do salário, caso isso ocorra avise com mensagem “Infelizmente  você não pode obter o 
# empréstimo”, se possível calcule o valor da prestação como sendo o valor  da casa a comprar dividido pelo 
# número de meses a pagar e exiba o valor da prestação, junto com a frase  “Empréstimo OK”.

valor_casa=float(input('Digite o valor da casa ou apartamento desejado:\n R$'))
salario=float(input('Digite o valor do seu salário liquido por mês: \n R$'))
tempo=int(input('Digite a quantidade de tempo que você deseja pagar seu imovel: '))

meses_pagamento = tempo*12
prestacao=valor_casa/meses_pagamento
limite=salario*0.30
if prestacao > limite:
    print('Infelizmente você não pode obter o empréstimo, fica pra próxima')
else:
    print(f'Parabéns, empréstimo ok e o valor da prestação será de R${prestacao: .2f} por mês')