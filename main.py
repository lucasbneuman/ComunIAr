import os
import glob
import concurrent.futures
from enviar_email import enviar_mensajes_email_desde_csv
from enviar_wsp import enviar_mensajes_whatsapp_desde_csv

def main():
    carpeta_csv = 'DB'
    archivos_csv = glob.glob(os.path.join(carpeta_csv, '*.csv'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Ejecutar enviar_mensajes_email_desde_csv() en un subproceso
        executor.submit(enviar_mensajes_email_desde_csv)

        # Esperar un tiempo mínimo antes de ejecutar enviar_mensajes_whatsapp_desde_csv()
        wait_time = 10  # Ajusta el valor a la cantidad de segundos que deseas esperar antes de enviar mensajes por WhatsApp
        print(f"In {wait_time} segundo(s) se abrirá WhatsApp para enviar el mensaje.")
        executor.submit(lambda: time.sleep(wait_time))

        # Ejecutar enviar_mensajes_whatsapp_desde_csv() en otro subproceso
        executor.submit(enviar_mensajes_whatsapp_desde_csv)

    print("Proceso completado.")

if __name__ == '__main__':
    main()

