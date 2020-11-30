import cv2

from ocr.types import Image


def add_rectangle(image: Image, x0, y0, w, h, color=(127, 127, 127), thickness=2):
    return cv2.rectangle(image, (x0, y0), (x0 + w, y0 + h), color, thickness)
