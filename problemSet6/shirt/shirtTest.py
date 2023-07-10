""" Working file, Combine two images by pasting one onto the other """

import sys
import os.path
import PIL
from PIL import Image
from sys import argv

try:
    script, foto, foto1 = sys.argv

    """ check file formats.
    use the os.path.splitext() method to split the file name into its base name and extension.
    """
    if os.path.splitext(foto)[1].lower() != os.path.splitext(foto1)[1].lower():
        sys.exit("Invalid output")

    """ if the inputs are correct, paste and save image """
    for formato in [".jpg", ".jpeg", ".png"]:
        if argv[1].endswith(formato) and argv[2].endswith(formato):
            # open images
            image = Image.open(foto)
            image2 = Image.open(foto1)

            # save the image size
            size = image2.size

            # resize and paste image
            image2 = PIL.ImageOps.fit(image2, size)
            image = PIL.ImageOps.fit(image, size)
            image.paste(image2, image2)

            # save and show new image
            image.save("after.jpg")
            image.show()
except (ValueError, FileNotFoundError) as e:
    # if not os.path.isfile(foto) or not os.path.isfile(foto1):
    # sys.exit("File does not exist")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check if input file 1 matches input file2 extention
    elif os.path.splitext(foto)[1].lower() != os.path.splitext(foto1)[1].lower():

        sys.exit("Input does not exist")
    # sys.exit(str(e))
