""" animate images """

# imports
import sys
from PIL import Image

# place to store images
images = []

# loop through the files passed with command-line
for arg in sys.argv[1:]: # skip the first items in the argv list
    # open image from argv 
    image = Image.open(arg)
    # add the image that was open
    images.append(image)
# animate the images 
# save the image as gif, save all of the images, append on top of eachother, duration of animation is 200milli seconds
images[0].save("walking.gif", save_all=True, append_images=[images[1]], duration=200)
    

