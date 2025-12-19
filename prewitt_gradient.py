import numpy as np

from filters import conv2d


KX = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
KY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)


def prewitt_gradient(luma):
    gx = conv2d(luma, KX)
    gy = conv2d(luma, KY)
    g = np.maximum(np.abs(gx), np.abs(gy))
    g_max = np.max(g)
    if g_max > 0:
        g = g / g_max
    else:
        g = np.zeros_like(g)
    return g
