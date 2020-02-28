import cv2
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from functools import partial



caminho = ""


def pegar_imagem(botao):
    wind =  Tk()

    global caminho

    lb = Label(wind ,  text = "Digite o caminho da imagem : ")
    lb.pack()
    caminho = Entry(wind, width = 20 )
    caminho.pack()
    bt = Button(wind, text="OK", command=wind.destroy)
    bt.pack()
    
    wind.geometry("400x150")

    wind.mainloop()




def main_gui():

    #Cria Plat grafica
    root = Tk()
    root.title("Protótipo Íris")

    buttonA = Button(root,width = 30 , text = "ADD")
    buttonA["command"] = partial(pegar_imagem,buttonA)
    buttonA.pack(side=LEFT)

    

    if caminho != "" :
        print(caminho)
        img = cv2.imread(caminho)
        cv2.imshow(img)
    

    #define tamanho da tela
    root.geometry("600x400")

    root.mainloop()
    


   

    