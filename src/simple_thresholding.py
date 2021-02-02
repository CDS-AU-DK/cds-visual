#!/usr/bin/env python
"""
Exemplify thresholding, binarization of an grayscale image to either 0 or 255
--> select pixel value $p$ as threshold

Applications:
    - preprocessing, focus on objects or areas of particular interest in an image
    - segment foreground and background

Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain

"""
import numpy as np
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # remove high frequency edges with a blur kernel
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Image", image)
    # threshold
    (T, thres) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold Binary", thres)

    (T, thresInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Threshold Binary Inverse", thresInv)

    cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = thresInv))
    cv2.waitKey(0)

if __name__=="__main__":
    main()