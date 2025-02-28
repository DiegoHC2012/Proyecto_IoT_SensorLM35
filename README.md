# Proyecto_IoT_SensorLM35

Este repositorio es usado para almacenar y documentar el Proyecto realizado en la materia de IoT (Internet de las Cosas).

# Instrucciones de Uso:

## 1. Clonar el repositorio
Para obtener una copia local del proyecto, ejecuta el siguiente comando en la terminal (es necesario tener instalado git): 
 > git clone (url del repo)

## 2. Estructura del repositorio
Dentro del repositorio encontrarás las siguientes carpetas y archivos: 
- README.md: Archivo con la documentación y guía de uso.
- Main.py: Script principal para leer el sensor LM35 y enviar los datos a ThingSpeak.
- Matlab codes: Contiene el código para MathWorks.
  > Enviar email.txt: El envio de las alertas por correo al superar el limite.
  > Promedio de 10 temperaturas: El codigo para promediar las ultimas 10 temperaturas cada 30 minutos.

## 3. Instalación
Copia el archivo main.py del repositorio a la memoria del Raspberry utilizando de preferencia Thonny.

## 4, Instrucciones para el uso del código: 
- Modifica el archivo main.py con tus credenciales de red (SSID, PASSWORD) y la API key de ThingSpeak antes de ejecutarlo. (Asegúrate de tener las bibliotecas necesarias en tu entorno de MicroPython para ejecutar el código sin errores). 
- Ejecuta el codigo.
