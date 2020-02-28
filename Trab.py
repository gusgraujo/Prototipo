import cv2
import numpy as np
from tkinter import *
from matplotlib import pyplot as plt

root = Tk()
root.title('Processamento de imagem')

path = r'C:\_SourceCode\Prototipo\lena.jpg'

img = cv2.imread(path,1)
nimg = cv2.imread(path,0)


def colorido():
    cv2.imshow('image', img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def cinza():
    cv2.imshow('image', nimg) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def hist():
    plt.hist(nimg.ravel(),256,[0,256]); 
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def binario():    

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Black white image', blackAndWhiteImage)
      
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Retirar ruidos da imagem
def filter():    

    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    plt.subplot(121),plt.imshow(img)
    plt.subplot(122),plt.imshow(dst)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blur():    

    
    blur = cv2.blur(img,(5,5))

    plt.subplot(121),plt.imshow(img)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


b = Button(root, text="Colorido", command=colorido,height = 5, width = 25)
a = Button(root, text="Cinza", command=cinza,height = 5, width = 25)
j = Button(root, text="Binario", command=binario,height = 5, width = 25)
h = Button(root, text="Histograma", command=hist,height = 5, width = 25)
f1= Button(root, text="Passa-Baixo", command=filter,height = 5, width = 25)
f2= Button(root, text="Blur", command=blur,height = 5, width = 25)


j.pack()
b.pack()
a.pack()
h.pack()
f1.pack()
f2.pack()

w = Canvas(root, width=200, height=200) #Cria canvas com proporção
w.pack() #adiciona o canvas
root.mainloop()
