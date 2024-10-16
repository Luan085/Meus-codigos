def saude(saude,altura):
    indice = peso / (altura * altura)
    
    if(indice <18.5):
        print(f'Seu indice de massa corporal é de {indice: .1f} e você está magro.')
    elif(indice>=18.5 and indice<25):
        print(f'Seu indice de massa corpotal é de {indice: .1f} e você está bem. ')
    elif(indice>=25.5 and indice <30):
        print(f'Seu indice de massa corporal é de{indice: .1f} e você está com sobrepeso')
    else:
        print(f'Seu indice de massa corporal é de {indice: .1f} e você está parecendo thais carla')


peso = float(input('Digite seu peso:\n'))
altura = float(input('Digite sua altura:\n'))
saude(peso,altura)