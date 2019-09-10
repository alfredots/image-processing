import numpy as np
import cv2, os, math
from Utils import Utils
from Operations import Operations
from Transformations import Transformations
from Aritmetics import Aritmetics

class Options:

    @staticmethod
    def getFilename(name):
        return {
            "minute": "base-de-imagens/minute.jpg",
            "troye": "base-de-imagens/troye.jpg",
            "minute2": "base-de-imagens/minute2.jpg",
            "troye2": "base-de-imagens/troye2.jpg",
            "art-angels": "base-de-imagens/art-angels.jpg",
        }.get(name, "not found")

    @staticmethod
    def amostragem():
        n = int(input("n do valor:"))
        img = cv2.imread(Options.getFilename("minute"), 0)
        amostra = Utils.amostragem(img, n)
        return amostra

    @staticmethod
    def quantizacao():
        img = cv2.imread(Options.getFilename("art-angels"), 0)
        cor = int(input("numero do cores:"))
        resultado = Utils.quantizacaoUniforme(img, cor)
        name, extension = os.path.splitext(Options.getFilename("art-angels"))
        path = 'imagens-geradas/'+name.split('/')[1]
        new_filename = '{name}-quantizado-{k}{ext}'.format(name=path, k=cor, ext=extension)
        print(new_filename)
        cv2.imwrite(new_filename, resultado)

    @staticmethod
    def components():
        img = cv2.imread(Options.getFilename("art-angels"), 0)
        resultado = Utils.connectedComponents(img)
        name, extension = os.path.splitext(Options.getFilename("art-angels"))
        path = 'imagens-geradas/'+name.split('/')[1]
        new_filename = '{name}-connected-components-{ext}'.format(name=path, ext=extension)
        cv2.imwrite(new_filename, resultado)
    
    @staticmethod
    def optionAritmetic(type):
        imgOne = cv2.imread(Options.getFilename("minute"), 1)
        imgTwo = cv2.imread(Options.getFilename("troye"), 1)
        
        if type == "soma":
            return Aritmetics.add(imgOne, imgTwo)
        if type == "sub":
            return Aritmetics.sub(imgOne, imgTwo)
        if type == "mult":
            return Aritmetics.mult(imgOne, imgTwo)
        if type == "div":
            return Aritmetics.div(imgOne, imgTwo)