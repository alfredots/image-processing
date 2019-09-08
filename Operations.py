import numpy as np 
import cv2

class Operations:

    @staticmethod
    def _or(imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        for i in range(rows):
            for j in range(cols):
                if(imgOne[i,j]==128 or imgTwo[i,j]==128):
                    imgThree[i,j] = 128

        return imgThree

    @staticmethod
    def _and (imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        for i in range(rows):
            for j in range(cols):
                if(imgOne[i,j]==128 and imgTwo[i,j]==128):
                    imgThree[i,j] = 128

        return imgThree

    @staticmethod
    def _xor (imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        for i in range(rows):
            for j in range(cols):
                a = imgOne[i,j]==128
                b = imgTwo[i,j]==128 
                if((a and not b) or (not a and b)):
                    imgThree[i,j] = 128

        return imgThree

    @staticmethod
    def _not (imgOne, imgTwo):
        imgThree = imgOne.copy()
        rows, cols = imgOne.shape
        
        for i in range(rows):
            for j in range(cols):
                a = imgOne[i,j]==128
                b = imgTwo[i,j]==128
                if(a and (not b)):
                    imgThree[i,j] = 128

        return imgThree