from PIL import Image, ImageFilter

befor = Image.open("yard.bmp")
after = befor.filter(ImageFilter.BoxBlur(6))
after.save("output.bmp")