def media(nota1,nota2,nota3):
    nota = (nota1+nota2+nota3) /3
    if (nota>=7):
        print(f'A sua média para passar era de 7 e sua média foi de {nota: .2f}, você foi aprovado')
    else:
        print(f'A sua média para passar era de 7 e sua média foi de {nota: .2f}, você foi para recuperação')
        

nota1 =float(input('Digite a nota da primeira unidade: '))
nota2= float(input('Digite a nota da segunda unidade: '))
nota3= float(input('Digite a nota da terceira unidade:'))

media(nota1,nota2,nota3)