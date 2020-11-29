from pathlib import Path
from typing import Union

import cv2
import numpy as np


def aspect_ratio(image: np.ndarray) -> float:
    height, width = image.shape[:2]
    return width / height


def is_grayscale(image: np.ndarray):
    return image.ndim == 2


def is_color(image: np.ndarray):
    return image.ndim == 3


def load_image(path: Union[str, Path]) -> np.ndarray:
    """Read an image in RGB mode as numpy array."""
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
