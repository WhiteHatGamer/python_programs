from PIL import Image, ImageFilter
file = Image.open("test.jpg")
blurredfile = file.filter(ImageFilter.BoxBlur(111))
blurredfile.save("out.jpg")
