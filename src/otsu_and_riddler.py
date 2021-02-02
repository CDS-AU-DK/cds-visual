#!/usr/bin/env python
"""
Otsu method for automatic estimation of $T$ threshold value
    - assumes two maxima of grayscale histogram & searches for optimal separation

Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain

"""
import numpy as np
import argparse
import mahotas
import cv2
from numpy.matrixlib.defmatrix import matrix

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    #preprocessing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5,5), 0)
    cv2.imshow("Image", image)

    # Otsu
    T = mahotas.thresholding.otsu(blurred)
    print("[INFO] Otsu's threshold {}".format(T))

    thresh = image.copy()
    thresh[thresh > T] = 255
    thresh[thresh < 255] = 0
    thresh = cv2.bitwise_not(thresh)
    cv2.imshow("Otsu", thresh)

    # Riddler-Calvard
    T = mahotas.thresholding.rc(blurred)
    print("[INFO] Riddler-Calvard: {}".format(T))
    thresh = image.copy()
    thresh[thresh > T] = 255
    thresh[thresh < 255] = 0
    thresh = cv2.bitwise_not(thresh)
    cv2.imshow("Riddler-Calvard", thresh)

    cv2.waitKey(0)

if __name__=="__main__":
    main()