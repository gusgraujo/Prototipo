import cv2
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from functools import partial
from PIL import Image, ImageTk


caminho = r"C:\_SourceCode\Prototipo\lena.jpg"



def main_gui():

    #Cria Plat grafica
    root = Tk()
    root.title("Protótipo Íris")
    root.configure(background = "blue")
    
    buttonA = Button(root,width = 30 , text = "ADD")
    buttonA["command"] = partial(pegar_imagem,buttonA)
    buttonA.pack(side=TOP)
    

    buttonImg = Button(root,width = 30 , text = "Show-Image")
    buttonImg["command"] = partial(mostrar_Imagem,buttonImg)
    buttonImg.pack(side=TOP)
    
 
    image = Image.open("C:\_SourceCode\Prototipo\lena.jpg")
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.pack()
    

    #define tamanho da tela
    root.geometry("600x400")

    root.mainloop()
    


   
def pegar_imagem(botao):
    wind =  Tk()

    lb = Label(wind ,  text = "Digite o caminho da imagem : ")
    lb.pack()

    caminho = Entry(wind, width = 20 )
    caminho.pack()

    bt = Button(wind, text="OK", command=wind.destroy)
    bt.pack()
    
    wind.geometry("400x150")
    wind.mainloop()


def mostrar_Imagem(botao):

    if caminho != "" :
        print(caminho)
        img = cv2.imread(caminho)
        imS = cv2.resize(img, (960, 540)) 
        cv2.imshow("Imagem",imS)
        cv2.waitKey()
