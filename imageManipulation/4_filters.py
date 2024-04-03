from PIL import Image, ImageFilter
# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

# image import
img = Image.open('imageManipulation/image/picture.jpg')

# basic filters
img_blur = img.filter(ImageFilter.BLUR)
img_contour = img.filter(ImageFilter.CONTOUR)
img_detail = img.filter(ImageFilter.DETAIL)
img_edge = img.filter(ImageFilter.EDGE_ENHANCE)
img_edge_more = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img_find_edges = img.filter(ImageFilter.FIND_EDGES)
img_emboss = img.filter(ImageFilter.EMBOSS)
img_sharp = img.filter(ImageFilter.SHARPEN)
img_smooth = img.filter(ImageFilter.SMOOTH)
img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)

# # rank filters
# image_filtered_min = img.filter(ImageFilter.MinFilter(size = 5))
# image_filtered_median = img.filter(ImageFilter.MedianFilter(size = 5))
# image_filtered_max = img.filter(ImageFilter.MaxFilter(size = 5))

# multiband
img_boxblur = img.filter(ImageFilter.BoxBlur(radius = 4))
img_gaussblur = img.filter(ImageFilter.GaussianBlur(radius = 10))
img_unsharp = img.filter(ImageFilter.UnsharpMask(radius = 4))

# combine filters: blur + emboss
image_emboss = img.filter(ImageFilter.EMBOSS)
image_emboss_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius = 2))

img_gaussblur.save('7.png')