""" library PIL import Image """
""" Problem Set 6: shirt.py """
import os.path
import sys
import PIL
from sys import argv
from PIL import Image


try:
    # set command-line variables
    script, foto, foto1 = argv
    
    # if inputs are valid
    if os.path.splitext(foto)[1].lower() != os.path.splitext(foto1)[1].lower():
        sys.exit("Input and output have different file extension")
    for formato in ['.jpg', '.jpeg', '.png']:
        if argv[1].endswith(formato) and  argv[2].endswith(formato):
            # if the file match open it
            image = Image.open(argv[1])
            image2 = Image.open(argv[2])

            # save the image size
            size = image2.size

            # resize argv 1
            image = PIL.ImageOps.fit(image, size)

            #paste the image
            image.paste(image2, image2)

            # save new emage
            image.save('style.png')

            # show the new image
            image.show()
except (ValueError, FileNotFoundError):
	if len(argv) < 3:
		sys.exit("Too few command-line arguments")
	if len(argv) > 3:
		sys.exit("Too many command-line arguments")
	if not argv[1].endswith(formato) and not argv[2].endswith(formato):
		sys.exit("File not found")

""" read and write command-line arguments """