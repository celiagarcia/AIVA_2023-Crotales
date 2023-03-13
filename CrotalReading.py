# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:00:30 2023

@author: Rebeca Villarraso

Example: input argument
                 --image_path="./TestSamples/0002.tif"
"""

import easygui   # Importar módulo EasyGui
import cv2 
import argparse

def load_image_gray(PATH, display):
    gray = cv2.imread(FILE_PATH, 0)
    if display == 1: show_image('gray', gray)
    return gray

def show_image(txt, image):
    cv2.imshow(txt, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def otsu_binarization(gray_image, display):
    ret, imgf = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    if display == 1: show_image('otsu', imgf)
    return imgf

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
    gray=load_image_gray(FILE_PATH, 1)
    binarized=otsu_binarization(gray,1)
    
