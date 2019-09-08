import numpy as np
import cv2, os, math

class Transformations:

    @staticmethod
    def translation(img, xt, yt):
        
        newImage = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        rows, columns, pixel = img.shape

        for i in range(rows):
            for j in range(columns):
                newX = int(i + xt)
                newY = int(j + yt)
                
                if newX < rows - 1 and newY < columns - 1 and newX >= 0 and newY >= 0:
                    newImage[newX][newY] = img[i][j]

        return newImage

    @staticmethod
    def scale(img, xe, ye):
        newImage = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        rows, columns, pixel = img.shape

        for i in range(rows):
            for j in range(columns):
                newX = int(i * xe)
                newY = int(j * ye)
                
                if newX < rows - 1 and newY < columns - 1 and newX >= 0 and newY >= 0:
                    newImage[newX][newY] = img[i][j]

        return newImage

    @staticmethod
    def rotate(img, teta):
        newImage = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        rows, columns, pixel = img.shape

        for i in range(rows):
            for j in range(columns):
                newX = int(i*math.cos(teta) - j*math.sin(teta))
                newY = int(i*math.sin(teta) + j*math.cos(teta))
                
                if newX < rows - 1 and newY < columns - 1 and newX >= 0 and newY >= 0:
                    newImage[newX][newY] = img[i][j]

        return newImage

    