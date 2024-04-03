from PIL import Image, ImageEnhance
# https://pillow.readthedocs.io/en/stable/reference/ImageEnhance.html

# image import
img = Image.open('imageManipulation/image/picture.jpg')

# create an enhancer
color_enhancer = ImageEnhance.Color(img) # vibrance
contrast_enhancer = ImageEnhance.Contrast(img) # contrast
brightness_enhancer = ImageEnhance.Brightness(img) # contrast
sharpness_enhancer = ImageEnhance.Sharpness(img) # contrast

# applying the enhancer
enhanced_image = brightness_enhancer.enhance(5)
enhanced_image.show()