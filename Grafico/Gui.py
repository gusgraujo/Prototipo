import cv2
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt
from functools import partial
from PIL import Image, ImageTk
from tkinter import Menu
import FunOpenCv


caminho = r"C:\_SourceCode\Prototipo\Samples\lena.jpg"



def main_gui():

    #Cria Plat grafica
    root = Tk()
 
    root.title("Protótipo Íris")
    root.configure(background = "Gray")

    menu = Menu(root)

    item = Menu(menu)
    item.add_command(label = 'Exit')
    
    buttonA = Button(root,width = 30 , text = "ADD")
    buttonA["command"] = partial(pegar_imagem,buttonA)
    buttonA.grid(column = 1 , row = 0)

    buttonC = Button(root,width = 30 , text = "Iris Recognition")
    buttonC["command"] = partial(achar_Iris,buttonC)
    buttonC.grid(column = 1 , row = 1)
    

    buttonImg = Button(root,width = 30 , text = "Show-Image")
    buttonImg["command"] = partial(mostrar_Imagem,buttonImg)
    buttonImg.grid(column = 0 , row = 0)

    buttonImg = Button(root,width = 30 , text = "2D Gabor-Wavelets")
    buttonImg["command"] = partial(mostrar_Imagem,buttonImg)
    buttonImg.grid(column = 0 , row = 0)
    
    
    labelA = Label(root,text = "Imagem Referencia :")
    labelA.grid(column = 2 , row = 3)

  
 
    image = Image.open("C:\_SourceCode\Prototipo\Samples\lena.jpg")
    image = image.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.grid(column = 2 , row = 6)

    

    root.config(menu=item)
    #define tamanho da tela
    root.geometry("800x600")

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
        img = cv2.imread(caminho,0)
        imS = cv2.resize(img, (960, 540)) 
        cv2.imshow("Imagem",imS)
        cv2.waitKey()

def achar_Iris(botao):
    FunOpenCv.Iris.recCircle(caminho)

def gabor_wavelets(botao):
    FunOpenCv.Iris.gabor()
    
