import customtkinter as ctk
import random

# Função----------------------------------------------------------------------
def advinhar_numero():
    palpite = int(numero.get())
    
    if palpite < numero_secreto:
        resultado.configure(text='Muito baixo, tente novamente.')
    elif palpite > numero_secreto:
        resultado.configure(text='Muito alto, tente novamente.')
    else:
        resultado.configure(text='Parabéns, você acertou!')
#-------------------------------------------------------------------------
numero_secreto = random.randint(1, 100)


janela = ctk.CTk()
janela.geometry('400x300')
janela.title('Jogo da Adivinhação')


ctk.CTkLabel(janela, text='Jogo da Adivinhação', 
             font=('Arial', 20),
             text_color= "white").pack(pady=10)

numero = ctk.CTkEntry(janela,
                      width=300,
                      height=30, 
                      placeholder_text='Digite um número:')
numero.pack(pady=10)

botao = ctk.CTkButton(janela, 
                    text='Enviar número',
                    command=advinhar_numero)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela, 
                        text='')
resultado.pack(pady=10)


janela.mainloop()