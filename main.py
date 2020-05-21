import numpy as np
from PIL import Image
import image_processing

img = Image.open('pictures/001-s.bmp')
#img.show()
paths = image_processing.get_images_paths('pictures')