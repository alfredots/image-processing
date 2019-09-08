import numpy as np
import cv2, os, math

class Utils:

    @staticmethod
    def quantizacaoUniforme(img, K):
        img = np.float32(img)
        quantized = img.copy()

        rows = img.shape[0]
        cols = img.shape[1]

        for i in range(rows):
            for j in range(cols):
                quantized[i,j] = (math.pow(2, K) - 1) * np.float32(img[i, j] - img.min()) / (img.max() - img.min())
                quantized[i,j] = np.round(quantized[i,j]) * int(256/math.pow(2,K))
            
        return quantized
    
    @staticmethod
    def amostragem(img, n):
        amostra = [lin[::n] for lin in img[::n]]
        return np.array(amostra)

    @staticmethod
    def connectedComponents(img):
        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        ret, labels = cv2.connectedComponents(img)

        #Map component labels to hue val
        label_hue = np.uint8(179*labels/np.max(labels))
        blank_ch = 255*np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

        #cvt to BGR for display
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

        #set bg label to black
        labeled_img[label_hue==0] = 0

        return labeled_img