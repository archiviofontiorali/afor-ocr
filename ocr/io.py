import numpy as np


def aspect_ratio(image: np.ndarray) -> float:
    height, width = image.shape[:2]
    return width / height
