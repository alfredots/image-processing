import numpy as np
import cv2, os, math

class Realce:


    @staticmethod
    def normalizaContraste(img, c, d):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns = img.shape

        a = img.min()
        b = img.max()

        for i in range(rows):
            for j in range(columns):
                newImage[i,j] = (img[i,j] - a)*((d-c)/(b-a)) + c
        return newImage 

    @staticmethod
    def negativo(img):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

        a = img.min()
        b = img.max()

        for i in range(rows):
            for j in range(columns):
                newImage[i,j] = 255 -img[i,j]

        return newImage 

    @staticmethod
    def fatorGama(img, c, y):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

        a = img.min()
        b = img.max()

        for i in range(rows):
            for j in range(columns):
                newImage[i,j] = math.pow(c*((img[i,j]*1.0)/b), y)*255

        return newImage

    @staticmethod
    def linear(img, G, D):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

        for i in range(rows):
            for j in range(columns):
                resultado = G *img[i,j] + D
                if resultado > 255:
                    resultado = 255
                newImage[i,j] = resultado
        return newImage

    @staticmethod
    def logaritmico(img):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

        for i in range(rows):
            for j in range(columns):
                resultado = 105.9612*np.log10(img[i,j]+1)
                if resultado > 255:
                    resultado = 255
                newImage[i,j] = resultado
        return newImage

    @staticmethod
    def quadratico(img):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

        for i in range(rows):
            for j in range(columns):
                resultado = (1/255)*(img[i,j]**2)
                if resultado > 255:
                    resultado = 255
                newImage[i,j] = resultado
        return newImage

    @staticmethod
    def raiz(img):
        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

        for i in range(rows):
            for j in range(columns):
                resultado = 15.9687*np.sqrt(img[i,j])
                if resultado > 255:
                    resultado = 255
                newImage[i,j] = resultado
        return newImage