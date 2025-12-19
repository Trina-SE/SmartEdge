import numpy as np


def load_image(path):
    try:
        import cv2  # type: ignore

        img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
        if img is None:
            raise ValueError(f"Failed to read image: {path}")
        if img.ndim == 2:
            return img.astype(np.float32), "gray"
        if img.shape[2] == 4:
            bgr = img[:, :, :3]
            return bgr.astype(np.float32), "bgr"
        return img.astype(np.float32), "bgr"
    except Exception:
        pass

    try:
        from PIL import Image  # type: ignore
    except Exception as exc:
        raise RuntimeError("Neither cv2 nor PIL is available for image I/O.") from exc

    img = Image.open(path)
    if img.mode == "L":
        return np.array(img, dtype=np.float32), "gray"
    if img.mode in ("RGB", "RGBA"):
        arr = np.array(img.convert("RGB"), dtype=np.float32)
        return arr[:, :, ::-1], "bgr"
    arr = np.array(img.convert("RGB"), dtype=np.float32)
    return arr[:, :, ::-1], "bgr"


def save_image(path, img, mode):
    out = np.clip(img, 0, 255).astype(np.uint8)
    try:
        import cv2  # type: ignore

        cv2.imwrite(str(path), out)
        return
    except Exception:
        pass

    try:
        from PIL import Image  # type: ignore
    except Exception as exc:
        raise RuntimeError("Neither cv2 nor PIL is available for image I/O.") from exc

    if mode == "gray":
        Image.fromarray(out, mode="L").save(path)
    else:
        rgb = out[:, :, ::-1]
        Image.fromarray(rgb, mode="RGB").save(path)
