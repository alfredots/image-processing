import numpy as np
import cv2, os, math

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

def quantizacaoUniforme2(img, K):
    a = np.float32(img)
    bucket = 256 / K
    quantizado = (a / (256 / K))
    return np.uint8*(quantizado)*bucket

if __name__ == "__main__":

    filename = "vapor.jpeg"
    cores = [1,2]

    for cor in cores:
        img = cv2.imread(filename, 0)
        resultado = quantizacaoUniforme(img, cor)
        name, extension = os.path.splitext(filename)
        new_filename = '{name}-quantizado-{k}{ext}'.format(name=name, k=cor, ext=extension)
        cv2.imwrite(new_filename, resultado)