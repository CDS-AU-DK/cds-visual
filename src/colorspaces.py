#!/usr/bin/env python
"""
Exemplify colorspaces
- Hue-Saturation-Value (HSV): how humans think and conceive of color
- L*a*b*: how humans perceive color


Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain

"""
import numpy as np
import argparse
import cv2
from numpy.matrixlib.defmatrix import _convert_from_string

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    cv2.imshow("Original", image)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imshow("L*a*b", lab)

    cv2.waitKey(0)

if __name__=="__main__":
    main()