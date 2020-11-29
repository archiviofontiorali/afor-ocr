import pathlib
from typing import Tuple, List

import ocr.io

from .types import Image, Path


def load_from_folder(path: Path) -> List[Tuple[str, Image]]:
    images = []
    for ext in ("png", "jpg"):
        for image_path in sorted(pathlib.Path(path).glob(fr"*.{ext}")):
            image = ocr.io.load_image(image_path)
            images.append((image_path.name[:-4], image))
    return images


def create_sample_image() -> Tuple[str, Image]:
    return "opencv", ocr.io.create_example_image((256, 256), text="OpenCV")
