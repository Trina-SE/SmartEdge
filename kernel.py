import numpy as np


def kernel_from_c(c):
    k = np.full((3, 3), -c / 8.0, dtype=np.float32)
    k[1, 1] = c
    return k
