import numpy as np 
import cv2

class Aritmetics:

    @staticmethod
    def add(img1, img2):
        newImage = np.zeros((img1.shape[0],img1.shape[1],img1.shape[2]), np.uint8)

        rows, columns, pixel = img1.shape
        
        for i in range(rows):
            for j in range(columns):
                newImage[i][j] = img1[i][j] + img2[i][j]

        return newImage