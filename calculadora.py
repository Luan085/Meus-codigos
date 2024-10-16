import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk


ctk.set_appearance_mode ('dark')
#----------------------funcao------------------------
def soma():
    n1 = float(num1.get())
    n2 = float(num2.get())
    calculo = n1+n2
    resultado.configure(text=f'O resultado da soma é {calculo: .2f}')

def subtracao():
    n1 = float(num1.get())
    n2 = float(num2.get())
    calculo2=n1-n2
    resultado.configure(text=f'O resultado da subtração é {calculo2: .2f}')

def multiplicacao():
    n1 = float(num1.get())
    n2 = float(num2.get())
    calculo3=n1*n2
    resultado.configure(text=f'O resultado da multiplicação é {calculo3: .2f}')

def divisao():
    n1 = float(num1.get())
    n2 = float(num2.get())
    calculo4=n1/n2
    resultado.configure(text=f'O resultado da divisão é {calculo4: 2f}')  


#-----------------------------------------------------

janela=ctk.CTk()
janela.geometry('500x500')
janela.resizable(width=False, height=False)


ctk.CTkLabel(janela,
             text = 'Calculadora para leigos',
             font = ('verdana', 26, 'bold'),
             text_color= 'white').pack(pady=10)

num1=ctk.CTkEntry(janela,
                     width=300,
                     height=30,
                     placeholder_text= 'Digite um número para operação:')
num1.pack(pady=10)

num2=ctk.CTkEntry(janela,
                     width=300,
                     height=30,
                     placeholder_text= 'Digite outro número para operação:')
num2.pack(pady=10)

bot1 = ctk.CTkButton(janela,
              text = 'Soma',
              width= 100,
              height=5,
              fg_color='black',

              command=soma)
bot1.place(x=10, y=150 )

bot2 = ctk.CTkButton(janela,
              text = 'Subtração',
              width= 100,
              height=5,
              fg_color='red',
              command= subtracao)
bot2.place(x=10 , y= 170)

bot3 = ctk.CTkButton(janela,
              text = 'Multiplicação',
              width= 100,
              height=5,
              fg_color='green',
              command= multiplicacao)
bot3.place(x=10, y=190)

bot4 = ctk.CTkButton(janela,
              text = 'Divisão',
              width= 100,
              height=5,
              fg_color='blue',
              command= divisao)
bot4.place(x=10,y=210)

resultado=ctk.CTkLabel(janela,
                       text='',
                       font= ('verdana', 20, 'bold'),
                       text_color='yellow',)
resultado.pack(pady=80)

janela.mainloop()