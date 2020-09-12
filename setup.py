from setuptools import setup

setup(
    name="afor-ocr",
    version="0.0.0",
    packages=["ocr"],
    zip_safe=False,
    python_requires=">=3.8.0",
    install_requires=["pytesseract"],
)
