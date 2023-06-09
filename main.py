import os
import glob
import concurrent.futures
from enviar_email import enviar_mensajes_email_desde_csv

def main():
    carpeta_csv = 'DB'
    archivos_csv = glob.glob(os.path.join(carpeta_csv, '*.csv'))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Ejecutar enviar_mensajes_email_desde_csv() en un subproceso
        executor.submit(enviar_mensajes_email_desde_csv)

    print("Proceso completado.")

if __name__ == '__main__':
    main()


