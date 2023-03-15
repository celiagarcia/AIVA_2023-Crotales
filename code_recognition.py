'''
AIVA_2023-Crotales
@author: Rebeca Villarraso / Celia Garcia
'''
import cv2
import pytesseract



def recognition(img_prep):

    custom_config = r'--oem 3 --psm 6'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    num_crotal_text = pytesseract.image_to_string(img_prep, config=custom_config)

    return num_crotal_text
