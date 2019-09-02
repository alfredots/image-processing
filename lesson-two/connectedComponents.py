import cv2
import os
import numpy as np 

filename = 'art-angels.jpg'
img = cv2.imread(filename, 0)
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

#cv2.imshow('labeled.png', labeled_img)
name, extension = os.path.splitext(filename)
new_filename = '{name}-labeled{ext}'.format(name=name, ext=extension)
cv2.imwrite(new_filename, labeled_img)
#cv2.waitKey()