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
