import os
from pathlib import Path
from PIL import Image
import numpy as np
from matplotlib import image as mpimg

PATH = Path(__file__).parent
IMAGE_PATH = PATH / 'resources' / 'input'


def load_data(image_target: str):
    analyse_image = os.path.join(IMAGE_PATH, image_target)
    return mpimg.imread(analyse_image)


def load_image(image_target: str) -> np.ndarray:
    analyse_image = os.path.join(IMAGE_PATH, image_target)
    Image.open(analyse_image).show()
    # return np.asarray(Image.open(analyse_image).convert('RGB'))
    # return np.asarray(Image.open(analyse_image))


def remove_extra_band(im_array: np.ndarray) -> np.ndarray:
    return im_array[:, 0:3]


def show_image(image_array: np.ndarray, title: str = 'Image'):
    Image.fromarray(image_array).show(title)


def transform_float_to_uint8(im_array: np.ndarray) -> np.ndarray:
    return (im_array * 255 / np.max(im_array)).astype('uint8')
