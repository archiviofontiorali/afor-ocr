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


def create_example_image(shape=(256, 256), text: str = None):
    """Generate a simple gradient image with some optional text."""
    width, height = shape
    image = np.empty((height, width, 3), dtype=np.uint8)

    colors = (
        np.array([255, 0, 0], dtype=np.uint8),
        np.array([0, 255, 0], dtype=np.uint8),
    )
    for j in range(height):
        image[j, ...] = (j / 255) * colors[0] + (1 - j / 255) * colors[1]

    if text:
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 255, 255)
        cv2.putText(image, text, (10, height // 2), font, 2, color, 2, cv2.LINE_AA)

    return image
