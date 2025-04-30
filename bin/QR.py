import qrcode

qr = qrcode.QRCode(version=3)

print("-"*30)
print("example: https://google.com ")
QRLINK = input("URL: ")

qr.add_data(QRLINK)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR.png")

