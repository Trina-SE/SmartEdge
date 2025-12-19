import numpy as np


def _sliding_window_view(arr, k):
    try:
        return np.lib.stride_tricks.sliding_window_view(arr, (k, k))
    except Exception:
        return None


def median_filter_3x3(img):
    windows = _sliding_window_view(np.pad(img, 1, mode="reflect"), 3)
    if windows is not None:
        return np.median(windows, axis=(-2, -1))
    out = np.empty_like(img)
    padded = np.pad(img, 1, mode="reflect")
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.median(padded[i : i + 3, j : j + 3])
    return out


def max_filter(img, k):
    pad = k // 2
    windows = _sliding_window_view(np.pad(img, pad, mode="reflect"), k)
    if windows is not None:
        return np.max(windows, axis=(-2, -1))
    out = np.empty_like(img)
    padded = np.pad(img, pad, mode="reflect")
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.max(padded[i : i + k, j : j + k])
    return out


def conv2d(img, kernel):
    try:
        import cv2  # type: ignore

        return cv2.filter2D(img, ddepth=-1, kernel=kernel, borderType=cv2.BORDER_REFLECT)
    except Exception:
        pass
    try:
        from scipy import ndimage  # type: ignore

        return ndimage.convolve(img, kernel, mode="reflect")
    except Exception:
        pass
    if kernel.shape == (3, 3):
        padded = np.pad(img, 1, mode="reflect")
        out = np.empty_like(img)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                patch = padded[i : i + 3, j : j + 3]
                out[i, j] = np.sum(patch * kernel)
        return out
    raise RuntimeError("No convolution backend available for kernel size.")
