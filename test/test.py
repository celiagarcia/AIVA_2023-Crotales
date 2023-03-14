'''
AIVA_2023-Crotales
Celia Garcia / Rebeca Villarraso
Descripcion del fichero: conjuntos de test unitarios para la aplicacion CrotalReading.
Estatus actual: Fase inicial, solo la definicion de los test que se van a llevar a cabo.
'''

import unittest

class ImageReadingTest(unittest.TestCase):
    '''Realiza los test al bloque image_reading'''

    def test_read_arguments(self):
        '''Prueba que se leen bien todos los argumentos'''
        return
    
    def test_read_tif(self):
        '''Prueba que se lee una imagen en formato tif'''
        return
    
    def test_read_path(self):
        '''Prueba que el path de la imagen es correcto'''
        return
    
    def test_read_gray(self):
        '''Prueba que se lee una imagen en escala de grises'''
        return
    

class CrotalCodeRecognition(unittest.TestCase):
    '''Realiza los test al bloque crotal_code_recognition'''

    def test_preprocessing_image(self):
        '''Prueba que se preprocesa la imagen, obteniendo una imagen binaria'''
        return
    
    def test_detect_region_code(self):
        '''Prueba que se detecta unicamente una region valida del codigo del crotal'''
        return

    def test_recognition_crotal_code(self):
        '''Prueba que se reconoce un codigo numerico correspondiente a la region detectada'''
        return
    
    def test_crotal_code_recognition_four_numbers(self):
        '''Prueba que el codigo reconocido es de cuatro digitos'''
        return


class CodeToTxtTest(unittest.TestCase):
    '''Realiza los test al bloque code_to_txt'''

    def test_create_txt(self):
        '''Prueba que se genera el fichero CrotalCode.txt'''
        return
    
    def test_write_code_to_txt(self):
        '''Prueba que se escribe el codigo numerico en el fichero txt'''
        return


class CrotalReadingTest(unittest.TestCase):
    '''Realiza los test al sistema completo CrotalReading.exe'''

    def test_crotal_reading_ground_truth(self):
        '''Prueba que se ejecuta la aplicacion completa al introducir un input, obteniendo un resultado'''
        return
    
    def test_crotal_reading_ground_truth(self):
        '''Compara el codigo numerico obtenido por el sistema con el codigo del GroundTruth'''
        return
    
    def test_crotal_reading_time(self):
        '''Prueba que tarda menos de un minuto en obtener el resultado'''
        return

if __name__ == "__main__":
    unittest.main()