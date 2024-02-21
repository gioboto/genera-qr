import qrcode

def generar_qr(texto, nombre_archivo):
    # Crear un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Agregar los datos (texto) al QRCode
    qr.add_data(texto)
    qr.make(fit=True)

    # Crear una imagen del código QR
    imagen = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen del código QR
    imagen.save(nombre_archivo)

