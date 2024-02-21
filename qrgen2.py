import pyqrcode
from PIL import Image

def generar_qr(texto, nombre_archivo):
    # Generar el código QR
    qr = pyqrcode.create(texto)

    # Guardar el código QR en un archivo de imagen PNG
    qr.png(nombre_archivo, scale=10)

