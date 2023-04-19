# Reconocimiento de dígitos en imágenes de crotales
:woman_student: Proyecto para la asignatura ‘Aplicaciones Industriales y Comerciales de la Visión Artificial’ del Máster Universitario en Visión Artificial de la URJC, impartida entre enero y abril de 2023.

[Project AIVA_2023-Crotales](https://github.com/users/celiagarcia/projects/1/views/5?layout=board) para ayudar a planificar y hacer seguimiento del trabajo.

## Descripción
Dentro del actual *Sistema de Identificación de Vacunos*, se nos pide la implementación de una solución que mejore el rendimiento de lectura de códigos de identificación animal, leyendo los códigos a partir de unas imágenes de entrada y los retorne como código numérico.

Este proyecto consiste en desarrollar dicha aplicación, que llamaremos **CrotalReading.exe**, para el reconocimiento de dígitos situados en la parte inferior de los crotales de ganadería vacuna, con ayuda del dataset proporcionado por el cliente.

Esta aplicación será integrada en el actual *Sistema de Identificación de Vacunos* para que en lugar de realizar la lectura de crotales actual, realice la llamada a la aplicación CrotalReading.exe, lea el código de la imagen del crotal y este código se proporcione a su programa de Visual Basic que continuará con el proceso habitual.
![general_block_diagram](images/general_block_diagram.jpg)

## Dataset
El conjunto de datos que nos ha proporcionado el cliente está compuesto por 397 imágenes de crotales con sus respectivas etiquetas. Las imágenes son en formato TIF, escala de grises, 640x480, 8 bits.

![example_dataset](images/example_dataset.jpg)

##  Documentación
Documentación del proyecto entregada al cliente:
- :page_facing_up: Documento de Requisitos del Sistema (DRS) y Presupuesto.

## Estructura del proyecto

    .
    ├── images
    │        ├── example_dataset.jpg
    │        └── general_block_diagram.jpg
    ├── test
    │        └── test.py
    ├── README.md
    ├── code_detector.py
    ├── code_recognition.py
    ├── crotal_code_recognition_main.py
    ├── image_preprocessing.py
    ├── main.py


## Cómo ejecutar la aplicación
1. Copiar el fichero CrotalCodeExtractor.exe en el PC dónde se ejecuta la aplicación Visual Basic cliente.
  Descargar de:
  https://urjc-my.sharepoint.com/:u:/g/personal/r_villarraso_2021_alumnos_urjc_es/Ea1YMgjxtrpArgxO2WYkzP8BH3ajuyRiYODtGDcfGzcuyg
3. En la misma ubicación crear una carpeta nueva por defecto llamarla "Codes".
4. En la misma ubicación crear una carpeta nueva por defecto llamarla "TestSamples". En esta carpeta se guardarán las imágenes de test.
5. Abrir la consola Windows (PowerShell o cmd) y situarse en la ubicación del fichero CrotalCodeExtractor.exe.
6. Introducir la siguiente línea de comando por defecto:
CrotalCodeExtractor.exe --image_path='./TestSamples/' --image_name='0001.tif' --output_path='./Codes/' --pytesseract_path='C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
6. Si alguno de los parámetros anteriores, no es indicado "por defecto" o la ruta del ejecutable de tesseract.exe está en otra ubicación, indicarlo en los parámetros:
--image_path = ruta dónde se ubican las imágenes a leer
--image_name = nombre de imagen a leer
--output_path= ruta dónde se guardarán los códigos leídos
--pytesseract_path = ruta dónde se ubica el fichero tesseract.exe
7. También se puede ejecutar la misma aplicación desde la consola Python con los mismos parámetros y desde el archivo principal CrotalCodeExtractor.py

## Test
Los test automáticos pueden ejecutarse desde el fichero Testing_CrotalCodeExtractor.exe o bien desde la consola Python con el archivo Testing_CrotalCodeExtractor.py.
  Descargar de: 
  https://urjc-my.sharepoint.com/:u:/g/personal/r_villarraso_2021_alumnos_urjc_es/EVhQq-Vt6FpJnIU_ka6TUY4BHRofTFd5w0Rm2u9duherLQ

## Resultados
## Autoras
- :woman_technologist: Celia García Fernández: [celiagarcia](https://github.com/celiagarcia?tab=repositories)
- :woman_technologist: Rebeca Villarraso Jiménez: [RebekkaVision](https://github.com/RebekkaVision)

