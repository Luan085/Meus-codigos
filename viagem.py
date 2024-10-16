def viagem_total(distancia,consumo,preco):
    calculo = (distancia/consumo)*preco
    print(f'O valor total gasto na viagem será de R${calculo: .2f}')

distancia=float(input('Digite a distância que você irá percorrer:\n KM: ' ))
consumo = float(input('Digite o consumo que seu carro faz por litro:\n km/l: '))
preco= float(input('Digite o preço do litro da gasolina que você pagou:\n R$' ))

    
viagem_total (distancia,consumo,preco)
