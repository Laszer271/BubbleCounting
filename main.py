import numpy as np
from PIL import Image, ImageFilter
from skimage.filters import sobel
from skimage.feature import canny
from skimage import morphology

# normal image
img = Image.open('rys2.bmp')
img.show()

# edge detector from PIL ImageFilter
img_edges = img.filter(ImageFilter.FIND_EDGES)
img_edges.show()

# sobel filter from skimage.filters 
array = np.array(img)
array = sobel(array)
array = array * 255
img_sobel = Image.fromarray(array)
img_sobel.show()

# canny filter from skimage.feature
array = np.array(img)
array = canny(array, sigma=1.2) # sigma decides what information to delete
img_canny = Image.fromarray(array)
img_canny.show()

# canny filter after morphology dilation
for i in range(3):
    array = morphology.binary_dilation(array)
img_canny_dilated = Image.fromarray(array)
img_canny_dilated.show()
