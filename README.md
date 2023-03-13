# Reconocimiento de dígitos en imágenes de crotales
:woman_student: Proyecto para la asignatura ‘Aplicaciones Industriales y Comerciales de la Visión Artificial’ del Máster Universitario en Visión Artificial de la URJC, impartida entre enero y abril de 2023.

[Project AIVA_2023-Crotales](https://github.com/users/celiagarcia/projects/1/views/5?layout=board) para ayudar a planificar y hacer seguimiento del trabajo.

## Descripción
Dentro del actual *Sistema de Identificación de Vacunos*, se nos pide la implementación de una solución que mejore el rendimiento de lectura de códigos de identificación animal, leyendo los códigos a partir de unas imágenes de entrada y los retorne como código numérico.

Este proyecto consiste en desarrollar dicha aplicación, que llamaremos **CrotalReading.exe**, para el reconocimiento de dígitos situados en la parte inferior de los crotales de ganadería vacuna, con ayuda del dataset proporcionado por el cliente.

Esta aplicación será integrada en el actual *Sistema de Identificación de Vacunos* para que en lugar de realizar la lectura de crotales actual, realice la llamada a la aplicación CrotalReading.exe, lea el código de la imagen del crotal y este código se proporcione a su programa de Visual Basic que continuará con el proceso habitual. 

## Dataset
El conjunto de datos que nos ha proporcionado el cliente está compuesto por 397 imágenes de crotales con sus respectivas etiquetas. Las imágenes son en formato TIF, escala de grises, 640x480, 8 bits.

![example_dataset](images/example_dataset.jpg)

##  Documentación
Documentación del proyecto entregada al cliente:
- :page_facing_up: Documento de Requisitos del Sistema (DRS) y Presupuesto.

## Estructura del proyecto

    .
    ├── images
    │        └── example_dataset.jpg
    ├── test
    │        └── tipos_defectos.png
    ├── README.md


## Test
Los test unitarios llevados a cabo son:
- ddd
- hhh

## Cómo ejecutar la aplicación
## Resultados
## Autoras
- :woman_technologist: Celia García Fernández: [celiagarcia](https://github.com/celiagarcia?tab=repositories)
- :woman_technologist: Rebeca Villarrasco Jiménez: [RebekkaVision](https://github.com/RebekkaVision)

