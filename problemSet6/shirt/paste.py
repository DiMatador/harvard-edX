import PIL
# import image module from pillow
from PIL import Image

# import image module from pillow
from PIL import Image


""" Example 1 """
# open the image1
Image1 = Image.open('before.jpg')
# make a copy the image so that the
# original image does not get affected
Image1copy = Image1.copy()

# open image2
Image2 = Image.open('shirt.png')
# make a copy the image so that the
# original image does not get affected
Image2copy = Image2.copy()

# safe the size of the image into variable size
size = Image2copy.size

# resize Image1copy
Image1copy = PIL.ImageOps.fit(Image1copy, size) # the foto.png

# paste image giving dimensions
Image1copy.paste(Image2copy, Image2copy)

# save the image
Image1copy.save('after.png')

# show the images
Image1copy.show()



"""Example 2: Changing parameters to place the Image2 on face of the cat in the Image1."""
# open the image
# Image1 = Image.open('foto.png')
 
# # make a copy the image so that
# # the original image does not get affected
# Image1copy = Image1.copy()
# Image2 = Image.open('shirt.png')
# Image2copy = Image2.copy()
 
# # paste image giving dimensions
# Image1copy.paste(Image2copy, (70, 150))

# # show the image
# Image1copy.show()
# # save the image
# Image1copy.save('pasted.png')