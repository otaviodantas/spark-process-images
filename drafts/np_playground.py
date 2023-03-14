from filters import gaussian_kernel, sobel_filters
import numpy as np


if __name__ == '__main__':
    # print(gaussian_kernel(3, sigma=1.4))

    img_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(sobel_filters(img_array))