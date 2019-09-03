import numpy as np 
import cv2

def orOperation (imgOne, imgTwo):
    imgThree = imgOne.copy()
    rows, cols = imgOne.shape
    
    for i in range(rows):
        for j in range(cols):
            if(imgOne[i,j]==128 or imgTwo[i,j]==128):
                imgThree[i,j] = 128

    return imgThree

def andOperation (imgOne, imgTwo):
    imgThree = imgOne.copy()
    rows, cols = imgOne.shape
    
    for i in range(rows):
        for j in range(cols):
            if(imgOne[i,j]==128 and imgTwo[i,j]==128):
                imgThree[i,j] = 128

    return imgThree

def xorOperation (imgOne, imgTwo):
    imgThree = imgOne.copy()
    rows, cols = imgOne.shape
    
    for i in range(rows):
        for j in range(cols):
            a = imgOne[i,j]==128
            b = imgTwo[i,j]==128 
            if((a and not b) or (not a and b)):
                imgThree[i,j] = 128

    return imgThree

def notOperation (imgOne, imgTwo):
    imgThree = imgOne.copy()
    rows, cols = imgOne.shape
    
    for i in range(rows):
        for j in range(cols):
            a = imgOne[i,j]==128
            b = imgTwo[i,j]==128
            print(a,b) 
            if(a and (not b)):
                imgThree[i,j] = 128

    return imgThree

if __name__ == "__main__":

    filenameOne = "minute-quantizado-1.jpg"
    filenameTwo = "troye-quantizado-1.jpg"

    imgOne = cv2.imread(filenameOne, 0)
    imgTwo = cv2.imread(filenameTwo, 0)
    cv2.imshow('result.png',andOperation(imgOne, imgTwo))
    cv2.waitKey()