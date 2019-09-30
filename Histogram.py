import numpy as np
import cv2

class Histogram:


    @staticmethod
    def gerar(img):
        hist = np.zeros(256)
        rows, cols = img.shape
        for i in range(rows):
            for j in range(cols):
                hist[img[i,j]]+=1
        return hist
    
    @staticmethod
    def normaliza(img):
        hist = Histogram.gerar(img)
        return hist/(img.shape[0]*img.shape[1])

    @staticmethod
    def acumulado(img):
        normHist = Histogram.normaliza(img)
        for i in range(len(normHist)):
            if i!=0:
                normHist[i]+=normHist[i-1]
        return normHist

    @staticmethod
    def equaliza(img):
        accumHist = Histogram.acumulado(img)
        accumHist = np.round(accumHist*255)
        nImg = np.zeros(img.shape)
        rows, cols = img.shape
        for i in range(rows):
            for j in range(cols):
                nImg[i,j] = accumHist[img[i,j]]
        return nImg