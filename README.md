# AFOR OCR library
Contains computer vision utils (based on OpenCV) and an OCR class based on tesseract


## Installation
Install `tesseract` with OS package manager

```shell script
# Debian based distro (ubuntu, debian, raspberry pi OS, ...)
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev
$ sudo apt install tesseract-ocr-eng tesseract-ocr-ita tesseract-ocr-ita_old

# ArchLinux based distro
$ sudo pacman -S tesseract
$ sudo pacman -S tesseract-data-eng tesseract-data-ita tesseract-data-ita_old
```

Install virtual environment

```shell script
# For production usage
$ make bootstrap

# For development usage
$ make bootstrap-dev
```
