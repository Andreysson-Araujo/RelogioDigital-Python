#Relógio Pythom
from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

############# CORES ##############
cor1 = "#3d3d3d" # Preta
cor2 = "#fafcff" # Branca
cor3 = "#21c25c" # Verde
cor4 = "#eb463b" #Vermelha
cor5 = "#dedcdc" #Cinza
cor6 = "#3080f0" #Azul

fundo = cor1
cor = cor2

janela = Tk()
janela.title("")
janela.geometry("320x170")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

#Criando a primeira função e seus atributos
def relogio():

    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_Semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.configure(text=hora)
    l1.after(200, relogio)
    l2.configure(text=dia_Semana +" "+ str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text= " " , font=("digital-7 80"), bg = fundo, fg=cor4)
l1.grid(row = 0, column=0, sticky =NW, padx=5)

l2 = Label(janela, text="", font=("digital-7 20"), bg = fundo, fg=cor4)
l2.grid(row = 1, column=0, sticky =NW, padx=5)

relogio()
janela.mainloop()