import numpy as np
import cv2, os, math
from Utils import Utils
from Operations import Operations
from Transformations import Transformations

if __name__ == "__main__":

    print("escolha a ação:")
    print("1-amostragem")
    print("2-quantização")
    print("3-componentes conectados")
    print("4-operações")
    print("5-transformações")

    option = input()
    
    #amostragem
    if option == "1":
        filename = "base-de-imagens/minute.jpg"
        n = int(input("n do valor:"))
        img = cv2.imread(filename, 0)
        amostra = Utils.amostragem(img, n)
        cv2.imshow('result.jpg',amostra)
        cv2.waitKey()

    #quantização
    if option == "2":
        filename = "base-de-imagens/art-angels.jpg"
        img = cv2.imread(filename, 0)
        cor = int(input("numero do cores:"))
        resultado = Utils.quantizacaoUniforme(img, cor)
        name, extension = os.path.splitext(filename)
        path = 'imagens-geradas/'+name.split('/')[1]
        new_filename = '{name}-quantizado-{k}{ext}'.format(name=path, k=cor, ext=extension)
        print(new_filename)
        cv2.imwrite(new_filename, resultado)
    
    #componentes conectados
    if option == "3":
        filename = "base-de-imagens/art-angels.jpg"
        img = cv2.imread(filename, 0)
        resultado = Utils.connectedComponents(img)
        name, extension = os.path.splitext(filename)
        path = 'imagens-geradas/'+name.split('/')[1]
        new_filename = '{name}-connected-components-{ext}'.format(name=path, ext=extension)
        print(new_filename)
        cv2.imwrite(new_filename, resultado)

    #operações
    if option == "4":
        print("1 - or")
        print("2 - and")
        print("3 - xor")
        print("4 - not")
        operation = input("digite a operação que deseja fazer:")
        filenameOne = "base-de-imagens/minute-2.jpg"
        filenameTwo = "base-de-imagens/troye-2.jpg"
        
        if operation == "1":
            imgOne = cv2.imread(filenameOne, 0)
            imgTwo = cv2.imread(filenameTwo, 0)
            cv2.imshow('result.png',Operations._or(imgOne, imgTwo))
            cv2.waitKey()
        
        if operation == "2":
            imgOne = cv2.imread(filenameOne, 0)
            imgTwo = cv2.imread(filenameTwo, 0)
            cv2.imshow('result.png',Operations._and(imgOne, imgTwo))
            cv2.waitKey()

        if operation == "3":
            imgOne = cv2.imread(filenameOne, 0)
            imgTwo = cv2.imread(filenameTwo, 0)
            cv2.imshow('result.png',Operations._xor(imgOne, imgTwo))
            cv2.waitKey()

        if operation == "4":
            imgOne = cv2.imread(filenameOne, 0)
            imgTwo = cv2.imread(filenameTwo, 0)
            cv2.imshow('result.png',Operations._not(imgOne, imgTwo))
            cv2.waitKey()

    #transformações
    if option == "5":
        print("1 - translação")
        print("2 - escala")
        print("3 - rotação")

        transformation = int(input("digite a operação que deseja fazer:"))
        filename = "base-de-imagens/art-angels.jpg"
        img = cv2.imread(filename, 1)
        
        if transformation == 1:
            print("--traslação--")
            xt = int(input("movimentação em x: "))
            yt = int(input("movimentação em y: "))
            resultado = Transformations.translation(img, xt, yt)
            cv2.imwrite('imagens-geradas/TRANS_X{x}_Y{y}.jpg'.format(x = xt, y = yt),resultado)
        
        if transformation == 2:
            print("--escala--")
            xe = int(input("escala em x: "))
            ye = int(input("escala em y: "))
            resultado = Transformations.scale(img, xe, ye)
            cv2.imwrite('imagens-geradas/SCALE_X{x}_Y{y}.jpg'.format(x = xe, y = ye),resultado)
        
        if transformation == 3:
            print("--rotação--")
            teta = int(input("valor do teta: "))
            resultado = Transformations.rotate(img, teta)
            cv2.imwrite('imagens-geradas/ROTATE_TETA{teta}.jpg'.format(teta = teta),resultado)
        