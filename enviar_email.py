import csv
import smtplib
import glob

def enviar_correo(destinatario, asunto, mensaje):
    remitente = 'lucasbneuman@gmail.com'
    password = 'gwkujqwybzoxdodw'

    cuerpo_correo = f"""\
    From: {remitente}
    To: {destinatario}
    Subject: {asunto}

    {mensaje}
    """

    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario, cuerpo_correo.encode('utf-8'))


def enviar_mensajes_email_desde_csv():
    archivos_csv = glob.glob('DB/*.csv')

    for archivo_csv in archivos_csv:
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)

            for fila in lector_csv:
                correo_electronico = fila['email']
                tiene_sitio_web = fila['website']

                if tiene_sitio_web:
                    asunto = "Correo de prueba - Sitio web disponible"
                    mensaje = "Hola, encontré su sitio web y me gustaría ofrecerle nuestros servicios relacionados. ¿Podemos programar una reunión para discutir los detalles?"
                else:
                    asunto = "Correo de prueba - Sin sitio web"
                    mensaje = "Hola, me gustaría ofrecerle nuestros servicios. Aunque no encontré un sitio web para su negocio, podemos discutir más detalles por teléfono. ¿Podemos hablar en breve?"

                if correo_electronico:
                    enviar_correo(correo_electronico, asunto, mensaje)

if __name__ == '__main__':
    enviar_mensajes_email_desde_csv()

