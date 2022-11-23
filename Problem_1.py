import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("0.png")
print(pytesseract.image_to_string(img,lang= 'rus'))
cv2.imshow('Image', img)
cv2.waitKey(0)
