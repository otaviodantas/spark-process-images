from typing import List

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


def visualize(imgs: List):
    plt.figure(figsize=(20, 40))
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1, 2, 0)
        plt_idx = i+1
        plt.subplot(4, 2, plt_idx)
        plt.imshow(img, cmap=matplotlib.cm.gray, vmin=0, vmax=255)
    plt.show()



