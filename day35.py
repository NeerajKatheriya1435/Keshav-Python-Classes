import qrcode
text = input("Enter the text: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=8,
)

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="orange")
img.save("rohan1.png")