import os
from typing import Iterable, List

import numpy

from filters import non_max_suppression, threshold, hysteresis, gaussian_kernel, sobel_filters
from utils import load_image, remove_extra_band, show_image, transform_float_to_uint8

from pyspark import SparkContext, SparkConf


def concat(iter_) -> numpy.ndarray:
    raw_data = iter_.collect()
    return numpy.concatenate(raw_data, axis=0)


if __name__ == '__main__':
    # os.putenv('PYDEVD_USE_CYTHON', 'YES')
    # conf = SparkConf().setAppName("collect").setMaster("local[*]")
    # sc = SparkContext(conf=conf)

    # image = load_image('test-gray-rgba.png')
    image = load_image('t1.tiff')

    # rdd = sc.parallelize(image)
    # rdd1 = rdd.map(remove_extra_band)
    #
    # rdd2 = rdd1.map(sobel_filters)
    # show_image(transform_float_to_uint8(numpy.asarray(rdd2.collect())), 'gaussian')
    #
    # rdd3 = rdd2.map(threshold)
    # show_image(transform_float_to_uint8(numpy.asarray(rdd3.collect())), 'gaussian')
    #
    # rdd4 = rdd3.map(hysteresis)
    # show_image(transform_float_to_uint8(numpy.asarray(rdd4.collect())), 'gaussian')
