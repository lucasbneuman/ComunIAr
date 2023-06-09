import csv
import pywhatkit
import glob
from datetime import datetime
import subprocess
import time

def enviar_mensaje_whatsapp(numero_telefono, mensaje):
    pywhatkit.sendwhatmsg(numero_telefono, mensaje, datetime.now().hour, datetime.now().minute + 1)

def enviar_mensajes_whatsapp_desde_csv():
    archivos_csv = glob.glob('DB/*.csv')

    for archivo_csv in archivos_csv:
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)

            for fila in lector_csv:
                numero_telefono = fila['phoneNumber']
                tiene_sitio_web = fila['website']

                if tiene_sitio_web:
                    mensaje = "Hola, encontré su sitio web y me gustaría ofrecerle nuestros servicios relacionados. ¿Podemos programar una reunión para discutir los detalles?"
                else:
                    mensaje = "Hola, me gustaría ofrecerle nuestros servicios. Aunque no encontré un sitio web para su negocio, podemos discutir más detalles por teléfono. ¿Podemos hablar en breve?"

                if numero_telefono:
                    enviar_mensaje_whatsapp(numero_telefono, mensaje)
                    time.sleep(30)  # Espera 30 segundos para que se envíe el mensaje
                    subprocess.call(['taskkill', '/F', '/IM', 'chrome.exe'])  # Cierra la ventana del navegador Chrome

if __name__ == '__main__':
    enviar_mensajes_whatsapp_desde_csv()


"""

def enviar_mensaje_whatsapp(numero_telefono, mensaje):
    pywhatkit.sendwhatmsg(numero_telefono, mensaje, datetime.now().hour, datetime.now().minute + 1)

def enviar_mensajes_whatsapp_desde_csv():
    archivos_csv = glob.glob('DB/*.csv')

    for archivo_csv in archivos_csv:
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)

            for fila in lector_csv:
                numero_telefono = fila['phoneNumber']
                mensaje = "¡Hola desde Python!"

                if numero_telefono:
                    enviar_mensaje_whatsapp(numero_telefono, mensaje)
                    time.sleep(10)  # Espera 10 segundos para que se envíe el mensaje
                    subprocess.call(['taskkill', '/F', '/IM', 'chrome.exe'])  # Cierra la ventana del navegador Chrome

if __name__ == '__main__':
    enviar_mensajes_whatsapp_desde_csv()

"""