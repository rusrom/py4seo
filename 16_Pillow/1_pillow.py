from PIL import Image


im = Image.open('smart4two.jpg')

# Size of image (WxH)
img_size = im.size

# Image width
img_width = im.width
# Image height
img_height = im.height

# Open image in imagemagick
# im.show()

# Save image with different colours
# im.save('boom.jpg')

# Save image with SAME colours
# im.save('boom_2.jpg', icc_profile=im.info.get('icc_profile'))

# Resize Image (Thumbnail)
import glob, os
size = 500, 500
im.thumbnail(size)
im.show()

# Mirror image
from PIL import ImageOps
res = ImageOps.mirror(im)
res.show()
