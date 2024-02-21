import qrgen1 as qr1
import qrgen2 as qr2

if __name__ == "__main__":
    # Texto que deseas codificar en el código QR
    texto = "¡Hola, mundo!"

    # Nombre del archivo donde se guardará el código QR (puede ser en formato PNG, JPG, etc.)
    nombre_archivo1 = "codigo_qr1.png"
    nombre_archivo2 = "codigo_qr2.png"
    # Generar el código QR
    qr1.generar_qr(texto, nombre_archivo1)
    qr2.generar_qr(texto, nombre_archivo2)

    print(f"Código QR1 generado y guardado en '{nombre_archivo1}'.")
    print(f"Código QR2 generado y guardado en '{nombre_archivo2}'.")
    
