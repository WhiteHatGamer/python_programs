import os
import qrcode

path = os.path.dirname(__file__)
img = qrcode.make("https://youtu.be/xvFZjo5PgG0")

img.save(f"{path}\qr.png", "PNG")
os.system(f"{path}\qr.png")