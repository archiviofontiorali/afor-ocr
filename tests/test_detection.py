import cv2
import pytest

from demo.images import create_sample_image
from ocr.tesseract import Tesseract, Word
from ocr.types import Image


@pytest.fixture
def image() -> Image:
    _name, image = create_sample_image()
    return image


@pytest.fixture
def extractor():
    return Tesseract()


def test_detect(image, extractor):
    assert isinstance(image, Image)
    assert hasattr(extractor, "detect")

    data = extractor.detect(image, lang="ita")
    assert isinstance(data, list)
    assert isinstance(data[0], Word)
