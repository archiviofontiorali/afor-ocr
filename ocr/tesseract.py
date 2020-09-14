import pytesseract


class Tesseract:
    def __init__(self, lang: str = "eng"):
        self.config = dict(
            lang=lang,
            # config="",
            # nice=0,
            # output_type=Output.STRING,
            # timeout=0,
            # pandas_config=None,
        )

    def convert(self, image) -> str:
        return pytesseract.image_to_string(image, **self.config)
