from PIL import Image

# Create new image by import
img = Image.open('imageManipulation/image/picture.jpg')

# # Alternative way to import an image
# with img.open('/imgs/picture.jpg') as img:
#     img.show()

# Create a new image from scratch
img_blank = Image.new('RGBA', (1200, 800))

# Show the picture
img_blank.show()

# Saving the picture
img.save('test_save.png')

# Image information
print(img.size)
print(img.filename)
print(img.format)
print(img.format_description)