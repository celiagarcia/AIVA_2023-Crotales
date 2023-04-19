# Reconocimiento de dígitos en imágenes de crotales
Proyecto para la asignatura ‘Aplicaciones Industriales y Comerciales de la Visión Artificial’ del Máster Universitario en Visión Artificial de la URJC, impartida entre enero y abril de 2023.

## Descripción
Este proyecto consiste en desarrollar una herramienta para el reconocimiento de los dígitos situados en la parte inferior de los crotales, con ayuda del dataset que nos ha proporcionado el cliente.

Para ello haremos una implementación en Python con [...]

Esta herramienta de reconocimiento será integrada en el sistema del cliente que necesita leer cada uno de los crotales que pasan por una cinta, para así identificarlos en su BBDD y emparejarlo con el cuerpo del animal. Así, se consigue automatizar y agilizar el proceso.

## Dataset
El conjunto de datos que nos ha proporcionado el cliente está compuesto por 397 imágenes de crotales con sus respectivas etiquetas. Las imágenes son en formato TIF, escala de grises, 640x480, 8 bits.

![example_dataset](images/example_dataset.jpg)

## Documentación
Documentación del proyecto entregada al cliente:
- Documento de requisitos y presupuesto: [...]

## Estructura del proyecto

## Cómo ejecutar la aplicación
1. Copiar el fichero CrotalCodeExtractor.exe en el PC dónde se ejecuta la aplicación Visual Basic cliente.
2. En la misma ubicación crear una carpeta nueva por defecto llamarla "Codes".
3. En la misma ubicación crear una carpeta nueva por defecto llamarla "TestSamples". En esta carpeta se guardarán las imágenes de test.
4. Abrir la consola Windows (PowerShell o cmd) y situarse en la ubicación del fichero CrotalCodeExtractor.exe.
5. Introducir la siguiente línea de comando por defecto:
CrotalCodeExtractor.exe --image_path='./TestSamples/' --image_name='0001.tif' --output_path='./Codes/' --pytesseract_path='C:\\Users\\bfzjs\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
6. Si alguno de los parámetros anteriores, no es indicado "por defecto" o la ruta del ejecutable de tesseract.exe está en otra ubicación, indicarlo en los parámetros:
--image_path = ruta dónde se ubican las imágenes a leer
--image_name = nombre de imagen a leer
--output_path= ruta dónde se guardarán los códigos leídos
--pytesseract_path = ruta dónde se ubica el fichero tesseract.exe
7. También se puede ejecutar la misma aplicación desde la consola Python con los mismos parámetros y desde el archivo principal CrotalCodeExtractor.py

## Test
Los test automáticos pueden ejecutarse desde el fichero Testing_CrotalCodeExtractor.exe o bien desde la consola Python con el archivo Testing_CrotalCodeExtractor.py.

## Resultados

## Autoras
- [Celia García Fernández](https://github.com/celiagarcia?tab=repositories)
- [Rebeca Villarrasco Jiménez](https://github.com/RebekkaVision)
