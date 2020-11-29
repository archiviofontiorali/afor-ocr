# AFOr OCR project
Contains computer vision utils (based on OpenCV) and an OCR class based on tesseract
Also contains a web application demo for AFOR OCR project built with holoviews and panel.

## Installation
Install `tesseract` on your system 
([documentation](https://tesseract-ocr.github.io/tessdoc/Downloads.html))
```Shell script
# ubuntu
$ sudo apt install tesseract-ocr libtesseract-dev
$ sudo apt install tesseract-ocr-eng tesseract-ocr-ita tesseract-ocr-ita_old

# archlinux  
$ sudo pacman -S tesseract
$ sudo pacman -S tesseract-data-eng tesseract-data-ita tesseract-data-ita_old
```

Install virtual environment

```shell script
# For production usage
$ make bootstrap
```

## Launch web interface
```shell script
$ make demo
```