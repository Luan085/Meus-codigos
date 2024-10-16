valor_produto=float(input('Digite o valor do produto: '))
forma_pagamento=float(input('Digite o número conforme o pagamento selecionado: \n 1 - À vista, com 10% de desconto\n 2- Parcelado em 2x, sem juros \n 3- Parcelado em 3x, com juros de 5% ao mês sobre o valor total: \n '))
porcentagem = 5/100
if forma_pagamento==1:
    print(f'O valor do seu produto com o desconto ficara: R${valor_produto - (valor_produto*10/100)}')
elif forma_pagamento ==2:
    print(f'O valor do seu produto ficará duas parcelas de R${valor_produto/2}')
else:
    #print(f'O valor do seu produto será divido em três parcelas de R${(valor_produto + porcentagem)/3: .2f}')
    print(f'O valor do seu produto ficará três parcelas de R${valor_produto/3: .2f} com mais 5% de juros ficará R${valor_produto * (1 + porcentagem): .2f}')