'''
AIVA_2023-Crotales
@author: Rebeca Villarraso / Celia Garcia
Example: input argument
                 --image_path="./TestSamples/0002.tif"
'''

import cv2
import easygui   # Importar módulo EasyGui
import argparse
import crotal_code_recognition_main


def image_reading(FILE_PATH):
    img_gray = cv2.imread(FILE_PATH, 0)
    show_image('img_gray', img_gray)
    return img_gray

def cotral_code_to_txt(num_crotal_code):
    return

def show_image(txt, image):
    cv2.imshow(txt, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":


    FILE_PATH = './TestSamples/0001.tif'  
    error=0

    parser=argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, default=FILE_PATH, help='Introduzca ruta de imagen del crotal')
    args = parser.parse_args()
    FILE_PATH = args.image_path 

    if FILE_PATH is None:
        easygui.msgbox("The path is empty, canceling image loading")
        error=1
    else:
        # IMAGE READING
        img_gray = image_reading(FILE_PATH)
        # CROTAL CODE RECOGNITION
        num_crotal = crotal_code_recognition_main.num_crotal_code(img_gray)
        # CROTAL CODE TO TXT
        cotral_code_to_txt(num_crotal)


        print("El número del crotal es: ", num_crotal)
        


