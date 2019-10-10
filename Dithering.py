import numpy as np
import cv2

class Dithering:
    
    @staticmethod
    def dithering(img):
        resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        rows, columns = img.shape
        
        for i in range(rows):
            for j in range(columns):
                temp = img[i][j] + np.random.randint(-127,127)
                threshold = 127
                if temp < threshold:
                    resultImage[i][j] = 0
                else:
                    resultImage[i][j] = 255
        return resultImage
    
    @staticmethod
    def aglomerado(img):   
        matrixP = np.array([[1,7,4],[5,8,3],[6,2,9]])
        
        resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        rows, columns = img.shape
        
        for i in range(rows):
            for j in range(columns):
                m = i % matrixP.shape[0]
                n = j % matrixP.shape[1]
                
                temp1 = (img[i][j] * 1.0)/255
                temp2 = (matrixP[m][n] * 1.0)/9
                
                if temp1 > temp2:
                    resultImage[i][j] = 255
                else:
                    resultImage[i][j] = 0
        return resultImage

    @staticmethod
    def dispersao(img):
        
        matrixP = np.array([[2,3],[4,1]])
        
        resultImage = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        rows, columns = img.shape
        
        for i in range(rows):
            for j in range(columns):
                m = i % matrixP.shape[0]
                n = j % matrixP.shape[1]
                
                temp1 = (img[i][j] * 1.0)/img.max()
                temp2 = (matrixP[m][n] * 1.0)/matrixP.max()
                
                if temp1 > temp2:
                    resultImage[i][j] = 255
                else:
                    resultImage[i][j] = 0
        return resultImage
