import cv2
import imutils
import numpy as np


def rotate(image: np.ndarray, angle: float, with_bounds=False, **kwargs):
    if with_bounds:
        return imutils.rotate_bound(image, angle)
    return imutils.rotate(image, angle, **kwargs)


def change_brightness(image: np.ndarray, alpha: float):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv[..., 2] = hsv[..., 2] * alpha
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return img


def change_saturation(image: np.ndarray, alpha: float):
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv[..., 1] = hsv[..., 1] * alpha
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return img


def crop(image: np.ndarray, x0, y0, x1=None, y1=None, w=None, h=None):
    if x1 is None and w is not None:
        x1 = x0 + w
    if y1 is None and h is not None:
        y1 = y0 + h
    return image[y0:y1, x0:x1]
