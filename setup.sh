#!/usr/bin/env bash
sudo apt-get update

# install required Linux binaries for OpenCV and Tesseract
sudo apt-get install -y python3-opencv
#sudo apt install -y tesseract-ocr
#sudo apt install -y libtesseract-dev

pip install -r requirements.txt