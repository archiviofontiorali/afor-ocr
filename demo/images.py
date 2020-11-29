import pathlib
from typing import List, Tuple

import cv2
import numpy as np

import ocr.io

from .types import Image, Path


def load_from_folder(path: Path) -> List[Tuple[str, Image]]:
    """Load all images from a specific folder."""
    images = []
    for ext in ("png", "jpg"):
        for image_path in sorted(pathlib.Path(path).glob(fr"*.{ext}")):
            image = ocr.io.load_image(image_path)
            images.append((image_path.name[:-4], image))
    return images


def create_sample_image(width=256, height=None, text="opencv") -> Tuple[str, Image]:
    """Generate a simple gradient image with some optional text."""
    if height is None:
        height = width
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

    return "opencv", image
