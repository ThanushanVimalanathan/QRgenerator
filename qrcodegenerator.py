import qrcode
import image

qr = qrcode.QRCode(
    version = 15,#version 15 means version of the qrcode
    box_size=10, # size of the box where qrcode will be displayed
    border=5
)


# path refers weg url
data = "www.youtube.com"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")