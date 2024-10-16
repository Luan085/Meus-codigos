#Cálculo de Preço de Compra no Supermercado 
#Implemente uma função que calcule o valor total de uma compra no supermercado. O programa deve  solicitar a
#distância de entrega em km, e o preço dos produtos comprados até digitar o preço com o valor  Zero. 
#O valor do frete é de R$ 2 por km para distâncias até 50 km, e R$ 1,80 para distâncias acima de 50  km. 
#Exiba o valor total da compra somado ao frete. 

def calcular_valor_total():
    distancia = float(input("Digite a distância de entrega em km: "))
    
    compra = 0
    contador = 0

    while True:
        produto = float(input("Digite o preço do produto ou 0 para finalizar: "))
        if produto == 0:
            break
        compra += produto
        contador += 1 

    if distancia <= 50:
        frete = 2 * distancia
    else:
        frete = 1.8 * distancia

    valor_total = compra + frete

    print(f"\nTotal de produtos comprados: {contador}")
    print(f"Valor total da compra: R$ {compra:.2f}")
    print(f"Valor do frete: R$ {frete:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
calcular_valor_total()