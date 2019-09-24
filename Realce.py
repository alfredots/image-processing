import numpy as np
import cv2, os, math

class Realce:


    @staticmethod
    def normalizaContraste(img, c, d):

        newImage = np.zeros((img.shape[0],img.shape[1]), np.uint8)
        rows, columns= img.shape

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
