import os
import collections
import six
from PIL import Image
import numpy as np

def is_iterable(arg):
    return (
        isinstance(arg, collections.Iterable) 
        and not isinstance(arg, six.string_types)
    )


def get_images_paths(input_path):
    final_images_paths = []
    
    items = []
    temp_items = []

    if is_iterable(input_path):
        temp_items.extend(input_path)
    else:
        temp_items.append(input_path)
    
    while len(temp_items):
        items = temp_items
        temp_items = []
        
        for item in items:
            extension = item[-4:]
            if extension != '.bmp':
                # we assume that item is actually a directory
                new_items = os.listdir(item)
                for new_item in new_items:
                    temp_items.append(item + f'/{new_item}')
            else:
                final_images_paths.append(item)
    
    return final_images_paths

def get_images(paths):
    images = []
    for path in paths:
        img = Image.open(path)
        images.append(img)
    return images

def get_arrays(paths):
    arrays = get_images(paths)
    arrays = [np.array(image) for image in arrays]
    return arrays