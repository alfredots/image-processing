import numpy as np 
import math

class Aritmetics:

    @staticmethod
    def add(img1, img2):
        newImage = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]), np.uint8)
        rows, columns, pixel = img1.shape

        for i in range(rows):
            for j in range(columns):
                newImage[i][j] = img1[i][j] + img2[i][j]

        return newImage 

    @staticmethod
    def sub(img1, img2):
        newImage = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]), np.uint8)
        rows, columns, pixel = img1.shape

        for i in range(rows):
            for j in range(columns):
                newImage[i][j] = img1[i][j] - img2[i][j]

        return newImage 

    @staticmethod
    def mult(img1, img2):
        newImage = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]), np.uint8)
        rows, columns, pixel = img1.shape

        for i in range(rows):
            for j in range(columns):
                newImage[i][j] = img1[i][j] * img2[i][j]

        return newImage

    @staticmethod
    def div(img1, img2):
        newImage = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]), np.uint8)
        rows, columns, pixel = img1.shape

        for i in range(rows):
            for j in range(columns):
                if img2[i][j][0] != 0:
                    newImage[i][j][0] = int(img1[i][j][0] / img2[i][j][0])
                else:
                    newImage[i][j][0] = img1[i][j][0]

                if img2[i][j][1] != 0:
                    newImage[i][j][1] = int(img1[i][j][1] / img2[i][j][1])
                else:
                    newImage[i][j][1] = img1[i][j][1]

                if img2[i][j][2] != 0:
                    newImage[i][j][2] = int(img1[i][j][2] / img2[i][j][2])
                else:
                    newImage[i][j][2] = img1[i][j][2]

        return newImage 