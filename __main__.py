# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:31:21 2023

@author: Rebeca Villarraso

PRACTICA 2: CROTALES

"""

import ProcessImage, ExportCode
from ProcessImage import *
from ExportCode import *

 # Constants   
image_path= './TestSamples/'  
image_name = '0002.tif'  
destination_folder='./Codes/'

if __name__ == '__main__':

    # Extract code
    proce=ProcessImage(image_path, image_name) 
    proce.otsu_binarization()
    code=proce.get_code()
    print('Codigo: ',code)
                    
    # Save code to txt
    my=ExportCode(image_name, destination_folder, code) 
    my.saveCodetoTxt()
                
        
    
    

    

 