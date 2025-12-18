# Adivina el Número

## Descripción del proyecto

Este proyecto consiste en un juego de adivinanza desarrollado en Python. El objetivo del programa es simular un juego en el que un jugador debe adivinar un número generado por el ordenador o por otro jugador, aplicando diferentes niveles de dificultad y registrando los resultados de cada partida.

El juego presenta un menú principal con las siguientes opciones:

1. Partida modo solitario
   - El número a adivinar es generado aleatoriamente por el ordenador.

2. Partida 2 Jugadores
   - Un jugador introduce un número a adivinar y otro jugador debe adivinarlo.

3. Estadística
   - Muestra los resultados de todas las partidas almacenadas en un archivo Excel (`Estadisticas.xlsx`).

4. Salir
   - Termina la ejecución del programa.

## Mecánica del juego

- El número a adivinar está entre 1 y 1000.  
- Tanto en el modo solitario como en el modo 2 jugadores, existe un submenú para elegir la dificultad:

Fácil: 20 intentos  
Medio: 12 intentos  
Difícil: 5 intentos

- El programa valida que las opciones elegidas por el usuario sean correctas y muestra un aviso si no lo son.  
- Durante la partida, se indica si el número buscado es mayor o menor que el intento del jugador.  
- Si el jugador adivina el número, gana la partida y se vuelve al menú principal.  
- Si se superan los intentos permitidos, se pierde la partida y se vuelve al menú principal.

## Registro de resultados

- Después de cada partida (se gane o se pierda), el programa solicita el nombre del jugador y guarda la información junto con el resultado en un archivo Excel llamado `Estadisticas.xlsx`.  
- La opción Estadística permite consultar los resultados almacenados y visualizar el historial de partidas.

## Archivos del proyecto

- `JuegoPrincipal.py` → archivo principal que ejecuta el juego.  
- `ModuloJuego.py` → módulo con las funciones necesarias para la lógica del juego.  
- `Estadisticas.xlsx` → archivo Excel donde se guardan los resultados de las partidas (se crea automáticamente si no existe).  
- `README.md` → descripción completa del proyecto.

## Librerías necesarias

- `openpyxl` → para la gestión de archivos Excel.  
- `matplotlib` → para generar gráficos estadísticos de las partidas (opcional).

Instalación:

pip install openpyxl matplotlib

## Cómo ejecutar el juego

En la terminal o en Jupyter Notebook, desde la carpeta del proyecto:

python JuegoPrincipal.py
