import cv2
import numpy as np
import pytesseract

per = 25

roi =[[(250, 334), (322, 356), 'text', 'Surname'], [(246, 382), (326, 402), 'text', 'Name'], [(252, 404), (312, 422), 'text', 'MiddleName']]


pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract'

imga=cv2.imread('0.png')
#h,w,c=imga.shape

image = imga.copy()
imagemask=np.zeros_like(image)

myData  = []
for x,r in enumerate(roi):
         cv2.rectangle(imagemask,((r[0][0]),r[0][1]),((r[1][0]),r[1][1]),(0,255,0) ,cv2.FILLED)
         image= cv2.addWeighted(image , 0.99 , imagemask,0.1,0)
         imgCrop = imga[r[0][1]:r[1][1],r[0][0]:r[1][0]]
         cv2.imshow(str(x),imgCrop)
         #imgCrop = cv2.resize(imgCrop, (w // 3, h // 3))

         if r[2] == 'text':
             print(f'{r[3]} :{pytesseract.image_to_string(imgCrop, lang="rus")}')
             myData.append(pytesseract.image_to_string(imgCrop , lang="rus"))

FinalData = []
for i in myData:
    FinalData.append(i.replace("\n", ""))

print(FinalData)


cv2.imshow("Output",imga)
cv2.waitKey(0)
