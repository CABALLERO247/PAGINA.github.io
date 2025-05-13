import qrcode

# Crear un código QR
data = "file:///C:/Users/llede/Downloads/EJEPLO/index1.html"
qr = qrcode.make(data)

# Guardar la imagen del QR
qr.save("codigo_qr.png")

print("Código QR generado y guardado como 'codigo_qr.png'")
