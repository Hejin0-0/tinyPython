from PIL import Image, ImageOps

# image import
img = Image.open('imageManipulation/image/picture.jpg')

# color changes
img_contrast = ImageOps.autocontrast(img = img, cutoff = 5)
img_inverted = ImageOps.invert(img)
img_solarize = ImageOps.solarize(img = img, threshold = 100)
img_posterize = ImageOps.posterize(img = img, bits = 1)
img_grayscale = ImageOps.grayscale(img = img)
img_equalized = ImageOps.equalize(img = img)
img_colorize = ImageOps.colorize(img = img.convert('L'), black = 'blue', white = 'red')

# dimension changes
img_mirror = ImageOps.mirror(img)
img_flip = ImageOps.flip(img)
img_scale = ImageOps.scale(img = img, factor = 0.4)
img_contain = ImageOps.contain(img = img, size = (500,200))

# Adding and removing
img_border = ImageOps.expand(img = img, border = 100, fill = (255,255,0))
img_padded = ImageOps.pad(img = img, size = (2500,1600))
img_fit = ImageOps.fit(img = img, size = (500,300))
img_crop = ImageOps.crop(img = img, border = 400)

img_flip.show()