'''
AIVA_2023-Crotales
@author: Rebeca Villarraso / Celia Garcia
Estado actual: preprocesa la imagen y reconoce los digitos.
    Falta implementar el detector de la secuencia de numeros que nos interesa.
'''
import image_preprocessing
import code_detector
import code_recognition



def num_crotal_code(img_gray):

    #preprocesar imagen
    img_prep = image_preprocessing.preprocessing(img_gray)

    #detectar codigo
    #output_code_detector = code_detector(output_code_detector)

    #reconocer/identificar numero del codigo
    num_crotal = code_recognition.recognition(img_prep)

    return num_crotal