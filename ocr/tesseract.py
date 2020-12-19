from typing import List

import pytesseract

from ocr.types import delegates


class Word:
    x0: int
    y0: int
    w: int
    h: int
    confidence: float
    text: str

    def __init__(self, x0, y0, w, h, confidence, text: str):
        self.x0, self.y0 = int(x0), int(y0)
        self.w, self.h = int(w), int(h)
        self.confidence = confidence
        self.text = text

    @property
    def x1(self) -> int:
        return self.x0 + self.w

    @property
    def y1(self) -> int:
        return self.y0 + self.h

    def __repr__(self):
        return (
            f"Word(({self.x0}, {self.y0}, {self.x1}, {self.y1}), "
            f"confidence={self.confidence}, text={self.text})"
        )


class Tesseract:
    def __init__(self, lang: str = "eng"):
        self.lang = lang

    @delegates(pytesseract.image_to_string)
    def extract(self, image, **kwargs) -> str:
        kwargs.setdefault("lang", self.lang)
        return pytesseract.image_to_string(image, **kwargs)

    @delegates(pytesseract.image_to_data)
    def detect(self, image, **kwargs) -> List[Word]:
        kwargs.setdefault("lang", self.lang)
        data: str = pytesseract.image_to_data(image, **kwargs)
        header, *rows = data.strip().split("\n")

        words = []
        for row in rows:
            x0, y0, w, h, confidence, text = row.split("\t")[-6:]
            words.append(Word(x0, y0, w, h, confidence, text))

        return words
