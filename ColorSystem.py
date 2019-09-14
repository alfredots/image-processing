import numpy as np
import cv2, os, math

class ColorSystem:

    @staticmethod
    def grayscale(img):
        newImage = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        rows, columns, pixel = img.shape

        for i in range(rows):
            for j in range(columns):
                red = img[i][j][0]
                green = img[i][j][1]
                blue = img[i][j][2]
                
                newPixel = round((red + green + blue) / 3)
                newImage[i][j] = newPixel

        return newImage

    @staticmethod
    def cmy(img):
        newImage = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        rows, columns, pixel = img.shape

        for i in range(rows):
            for j in range(columns):
                C = 255 - img[i][j][0]
                M = 255 - img[i][j][1]
                Y = 255 - img[i][j][2]
                
                newImage[i][j][0] = C
                newImage[i][j][1] = M
                newImage[i][j][2] = Y

        return newImage
    
    @staticmethod
    def YCrCb(img):
        newImage = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        rows, columns, pixel = img.shape

        delta = 128
        #delta = 32768
        #delta = 0.5

        for i in range(rows):
            for j in range(columns):
                R = img[i][j][0]
                G = img[i][j][1]
                B = img[i][j][2]

                Y= 0.229*R + 0.587*G + 0.144*B
                Cr = (R - Y) * 0.713 + delta
                Cb = (B - Y) * 0.564 + delta
                
                newImage[i][j][0] = Y
                newImage[i][j][1] = Cr
                newImage[i][j][2] = Cb

        return newImage
