# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:00:30 2023

@author: Rebeca Villarraso

Example: input argument
                 --image_path="./TestSamples/0002.tif"
"""

import easygui   # Importar módulo EasyGui
import cv2 as cv
import argparse

def load_image_gray(PATH, display):
    gray = cv.imread(FILE_PATH, 0)
    if display == 1:
        cv.imshow('gray', gray)
        cv.waitKey(0)
        cv.destroyAllWindows()
    

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
    load_image_gray(FILE_PATH, 1)
