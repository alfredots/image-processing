
import numpy as np
import cv2, os, math
from Utils import Utils
from Operations import Operations
from Transformations import Transformations
from Options import Options
import matplotlib.pyplot as plt

def showImage(name, img):
    cv2.imshow(name,img)
    cv2.waitKey()

def showHistogram(name, hist):
    x = np.arange(0, 256, 1)
    sub = plt.subplot()
    sub.bar(x, hist, 1, color = 'r')
    sub.set_title(name)
    plt.show()

if __name__ == "__main__":

    print("escolha a ação:")
    print("1-amostragem")
    print("2-quantização")
    print("3-componentes conectados")
    print("4-operações")
    print("5-transformações")
    print("6-aritmeticas")
    print("7-sistemas de cores")
    print("9-realces")
    print("10-histograma")
    print("11-dithering")
    print("12-filtros")

    option = input()
    
    #amostragem
    if option == "1":
        resultImage = Options.amostragem()
        showImage("amostragem", resultImage)

    #quantização
    if option == "2":
        Options.quantizacao()
        
    #componentes conectados
    if option == "3":
        Options.components()

    #operações
    if option == "4":
        print("1 - or")
        print("2 - and")
        print("3 - xor")
        print("4 - not")
        operation = input("digite a operação que deseja fazer:")
        filenameOne = "base-de-imagens/ball.jpg"
        filenameTwo = "base-de-imagens/triangle.jpg"
        
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
            cv2.imshow('result.png',Operations._not(imgOne))
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

    #aritmeticas
    if option == "6":
        print("1 - soma")
        print("2 - subtração")
        print("3 - multiplicação")
        print("4 - divisão")

        operation = int(input("digite a operação que deseja fazer:"))
        if operation == 1:
            resultImage = Options.optionAritmetic("soma")
            showImage("soma", resultImage)
        if operation == 2:
            resultImage = Options.optionAritmetic("sub")
            showImage("subtração", resultImage)
        if operation == 3:
            resultImage = Options.optionAritmetic("mult")
            showImage("multiplicação", resultImage)
        if operation == 4:
            resultImage = Options.optionAritmetic("div")
            showImage("divisão", resultImage)
    
    #sistema de cores
    if option == "7":
        print("1 - RGB pra Escala de cinza")
        print("2 - RGB pra CMY")
        print("3 - RGB pra YCrCb")

        operation = int(input("digite a conversão que deseja fazer:"))

        if operation == 1:
            resultImage = Options.optionSystemColor("grayscale")
            showImage("grayscale", resultImage)
        if operation == 2:
            resultImage = Options.optionSystemColor("cmy")
            showImage("CMY", resultImage)
        if operation == 3:
            resultImage = Options.optionSystemColor("ycrcb")
            showImage("YCrCb", resultImage)

    #realce
    if option == "9":
        print("1 - ajuste contraste")
        print("2 - negativo")
        print("3 - gama")
        print("4 - linear")
        print("5 - logaritimico")
        print("6 - quadratico")
        print("7 - raiz")

        operation = int(input("digite o realce que deseja aplicar:"))
        if operation == 1:
            originalImage,resultImage = Options.optionRealce("ajuste")
            showImage("original", originalImage)
            showImage("realce", resultImage)
        if operation == 2:
            originalImage,resultImage = Options.optionRealce("negativo")
            showImage("original", originalImage)
            showImage("realce", resultImage)
        if operation == 3:
            originalImage,resultImage = Options.optionRealce("gama")
            showImage("original", originalImage)
            showImage("realce", resultImage)
        if operation == 4:
            originalImage,resultImage = Options.optionRealce("linear")
            showImage("original", originalImage)
            showImage("realce", resultImage)
        if operation == 5:
            originalImage,resultImage = Options.optionRealce("log")
            showImage("original", originalImage)
            showImage("realce", resultImage)
        if operation == 6:
            originalImage,resultImage = Options.optionRealce("quadratico")
            showImage("original", originalImage)
            showImage("realce", resultImage)
        if operation == 7:
            originalImage,resultImage = Options.optionRealce("raiz")
            showImage("original", originalImage)
            showImage("realce", resultImage)

    #histograma
    if option == "10":
        print("1 - gerar histograma")
        print("2 - gerar histograma acumulado")
        print("3 - gerar imagem equalizada")
        operation = int(input("digite o realce que deseja aplicar:"))
        if operation == 1:
            originalImage,histogram = Options.optionHistograma("gera")
            showImage("original image", originalImage)
            showHistogram("original histogram", histogram)
        if operation == 2:
            originalImage,histogram = Options.optionHistograma("acumulado")
            showImage("original image", originalImage)
            showHistogram("acumulado histogram", histogram)
        if operation == 3:
            originalImage,equalizedImage = Options.optionHistograma("equalizado")
            showImage("original image", originalImage)
            showImage("equalized image", equalizedImage)

    #dithering
    if option == "11":
        print("1 - randomico")
        print("2 - aglomerado")
        print("3 - dispersao")
        operation = int(input("digite o dithering que deseja aplicar:"))
        if operation == 1:
            dithering = Options.optionDithering("normal")
            showImage("Dithering", dithering)
        if operation == 2:
            dithering = Options.optionDithering("aglomerado")
            showImage("Dithering", dithering)
        if operation == 3:
            dithering = Options.optionDithering("dispersao")
            showImage("Dithering", dithering)

    #filtros
    if option == "12":
        print("1 - media")
        print("2 - gaussiano")
        print("3 - mediana")
        operation = int(input("digite o filtro que deseja aplicar:"))
        if operation == 1:
            img = Options.optionFilters("media")
            cv2.imwrite('imagens-geradas/filtro-media.jpg'.format(),img)
        if operation == 2:
            img = Options.optionFilters("gaussiano")
            cv2.imwrite('imagens-geradas/filtro-gaussiano.jpg'.format(),img)
        if operation == 3:
            img = Options.optionFilters("mediana")
            cv2.imwrite('imagens-geradas/filtro-mediana.jpg'.format(),img)



cv2.destroyAllWindows()