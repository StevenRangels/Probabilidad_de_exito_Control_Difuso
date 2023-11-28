# Probabilidad de Exito en Contenido Audiovisual con Control Difuso

En este repositorio cuantificamos la probabilidad si una película será uno de los éxitos del año.

## EL problema planteado es el siguiente:

Eres un ingeniero de NETFLIX… y tienes el proyecto de cuantificar la probabilidad si una película será uno de los éxitos del año. Considerado como un indicador de éxito que la película hubiera tenido al menos 10 millones de visualizaciones en el primer mes de lanzamiento a nivel mundial. 

1. Variables de entrada: 
- Cantidad de visualizaciones. 
- Tiempo de estreno. 

2. Variable de salida: 
- Probabilidad de éxito.

## Diseñe un controlador difuso que cumpla los siguientes criterios: 

1. Diseña un controlador difuso que entregue el valor de probabilidad de éxito basado en la cantidad de visualizaciones y tiempo de estreno en meses.
2. Evalúa tu controlador difuso si la película al mes de ser lanzada tiene 800.000 visualizaciones. 
3. Evalúa tu controlador difuso si la película a los dos meses de ser lanzada y tiene 15 millones de visualizaciones 
4. Evalúa tu controlador difuso si la película a los 6 meses de ser lanzada y tiene 90 millones de visualizaciones. 

## Sistema de Predicción de Éxito con Lógica Difusa.

Este sistema utiliza lógica difusa en Python para determinar la probabilidad de éxito de una película en función de las variables de entrada: cantidad de visualizaciones y tiempo de estreno.

## Descripción de Contenido.

1. Carpeta "notebooks": Contiene el código fuente.
2. Carpeta "Images": Contiene imágenes de simulaciones.

## Descripción. 

El sistema de predicción de éxito utiliza lógica difusa para tomar decisiones basadas en la cantidad de visualizaciones y el tiempo de estreno de una película. La salida es la probabilidad de que la película sea considerada un éxito.

## Requisitos.

Asegúrate de tener Python y las siguientes bibliotecas instaladas:

pip install numpy scikit-fuzzy matplotlib

Se recomienda simular el código en Visual Studio Code.

## Detalles del Código

El código se divide en tres partes principales:

1. Definición de las Variables de Entrada y Salida.

Cantidad de visualizaciones y tiempo de estreno son variables de entrada que representan la cantidad de visualizaciones y el tiempo de estreno en meses. La probabilidad de exito es la variable de salida que representa el porcentaje de exito.

2. Funciones de Membresía.

Las funciones de membresía definen cómo se relacionan las entradas y la salida, estas están diseñadas en ciertos niveles para proporcionar mayor precisión en la segmentación.

3. Reglas Difusas.

El sistema utiliza reglas difusas para tomar decisiones basadas en las variables de entrada. Las reglas se definen para diferentes combinaciones de visualizaciones y tiempo.
