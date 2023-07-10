import sys
import os.path
import PIL
from PIL import Image
from sys import argv

""" image(.png, .jpg, jpeg) -> image(.png, jpg, jpeg) over layed
    Returns an image over layed with an other image
    >>> shirt.py before.png after.png
    after.png
    >>> shirt.py before1.jpg after.jpg
    after.jpg
    >>> shirt.py before2.jpeg after.jpeg
    after.jpeg
    >>> shirt.py before.jpg
    'To few comman-line arguments'
    >>> shirt.py before.jpg after.jpg error.error
    'To many command-line arguments'
    >>> shirt.py before.jpg after.txt
    'Input and outpu have different file extansions'
    >>> shirt.py before.txt after.jpg
    'File not found'
"""

try:
    # set command-line variable names
    script, photo, shirt = argv
    # check if the files are of the same type
    if os.path.splitext(photo)[1].lower() != os.path.splitext(shirt)[1].lower():
        sys.exit("Input and output have different file extensions")

    # add someting here later
    for formato in [".jpg", ".jpeg", ".png"]:
        if argv[1].endswith(formato) and argv[2].endswith(formato):
            # open muppet image
            image = Image.open(photo)
            # open shirt image
            shirt = Image.open("shirt.png")

            # save the images sizes
            # size = image.size
            shirt_size = shirt.size

            # muppet image rezise to fit shirt
            foto = PIL.ImageOps.fit(image, shirt_size)

            # paste the shirt on to muppet
            foto.paste(shirt, shirt)

            # save the pasted shirt onto muppet
            foto.save(argv[2])
            
            # open foto
            foto.show()

except (ValueError, FileNotFoundError):
    if len(argv) < 3:
        sys.exit("Too few command-line argumenets")
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")
    if not argv[1].endswith(formato) and not argv[2].endswith(formato):
        sys.exit("File not found")
