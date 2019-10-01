import numpy as np 
import cv2

class Operations:

    @staticmethod
    def binarizar(img):
        rows, cols = img.shape

        for i in range(rows):
            for j in range(cols):
                if(img[i,j] < 128):
                    img[i,j] = 0
                else:
                    img[i,j] = 255
        return img

    @staticmethod
    def _or(imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        imgOne = Operations.binarizar(imgOne)
        imgTwo = Operations.binarizar(imgTwo)

        for i in range(rows):
            for j in range(cols):
                if(imgOne[i,j]==255 or imgTwo[i,j]==255):
                    imgThree[i,j] = 255
                else:
                    imgThree[i,j] = 0

        return imgThree

    @staticmethod
    def _and (imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        imgOne = Operations.binarizar(imgOne)
        imgTwo = Operations.binarizar(imgTwo)

        for i in range(rows):
            for j in range(cols):
                if(imgOne[i,j]==255 and imgTwo[i,j]==imgOne[i,j]):
                    imgThree[i,j] = 255
                else:
                    imgThree[i,j] = 0
        return imgThree

    @staticmethod
    def _xor (imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        imgOne = Operations.binarizar(imgOne)
        imgTwo = Operations.binarizar(imgTwo)

        for i in range(rows):
            for j in range(cols):
                if( imgTwo[i,j]!=imgOne[i,j]):
                    imgThree[i,j] = 255
                else:
                    imgThree[i,j] = 0

        return imgThree

    @staticmethod
    def _not (imgOne):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        imgOne = Operations.binarizar(imgOne)

        for i in range(rows):
            for j in range(cols):
                imgThree[i,j] = 255 - imgOne[i,j]

        return imgThree