#Calculadora Gráfica de Conversão de Moeda com customtkinter 
#Utilizando o módulo customtkinter, crie uma calculadora gráfica para converter valores entre duas  moedas. A interface deve conter: 
#✔ Um campo de entrada para o valor em reais (R$). 
#✔ Um campo de entrada para o valor em dólar (US$) 
#✔ Um botão para converter o valor para dólares (US$). 
#✔ Um botão para converter o valor para Real (R$) 
#✔ Um campo que exiba o valor convertido.

import customtkinter as ctk

ctk.set_appearance_mode ('dark')
#----------------------funcao------------------------
def dolar():
    n1 = int(num1.get())
    calculo = n1*0.18
    resultado.configure(text=f'O resultado da conversao de real para dolar é {calculo: .2f}')

def real():
    n2 = int(num2.get())
    calculo2=n2*5.59
    resultado.configure(text=f'O resultado da conversão de dolar pra real é {calculo2: .2f}') 


#-----------------------------------------------------

janela=ctk.CTk()
janela.geometry('500x500')
janela.resizable(width=False, height=False)


ctk.CTkLabel(janela,
             text = 'Calculadora de valores',

             font = ('verdana', 22, 'bold'),
             text_color= 'white').pack(pady=10)

num1=ctk.CTkEntry(janela,
                     width=300,
                     height=30,
                     placeholder_text= 'Digite o valor em reais:')
num1.pack(pady=10)

num2=ctk.CTkEntry(janela,
                     width=300,
                     height=30,
                     placeholder_text= 'Digite o valor em dolar :')
num2.pack(pady=10)

bot1 = ctk.CTkButton(janela,
              text = 'Dolar',
              width= 100,
              height=5,
              fg_color='black',
              command=dolar)
bot1.place(x=10, y=150 )

bot2 = ctk.CTkButton(janela,
              text = 'Real',
              width= 100,
              height=5,
              fg_color='red',
              command= real)
bot2.place(x=10 , y= 170)


resultado=ctk.CTkLabel(janela,
                       text='',
                       font= ('verdana', 12, 'bold'),
                       text_color='yellow',)
resultado.pack(pady=50)

janela.mainloop()