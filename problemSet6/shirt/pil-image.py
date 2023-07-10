""" Problem set 6: Shirt.py """
import PIL
import sys
from sys import argv
from PIL import Image

# image load, remember that this only loads the file
im = Image.open("windows.jpg")
#print(im.format, im.size, im.mode)

# show the image
#im.show()
#print(im.show())

script, foto, outfit = argv

# open images
foto = Image.open(argv[1])
outfit = Image.open(argv[2])

# safe the size of the image into variable size
size = outfit.size

# resize images
resize = PIL.ImageOps.fit(foto, size) # the foto.png

my_shirt = PIL.ImageOps.fit(outfit, size) # the t-shirt


# paste style over foto
resize.paste(my_shirt, size)
#resize.show()

# save final image
resize.save("new.png")

# reading from an open file
# with open("shirt.png", "rb") as fp:
    # im = Image.open(fp)
    # # show the image
    # im.show()



