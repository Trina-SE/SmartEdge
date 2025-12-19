import numpy as np

from filters import max_filter


def retinex_contrast(luma, w):
    m = max_filter(luma, w)
    with np.errstate(divide="ignore", invalid="ignore"):
        phi = np.where(m > 0, 1.0 - (luma / m), 0.0)
    return np.clip(phi, 0.0, 1.0)
