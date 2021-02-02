#!/usr/bin/env python
"""

Methods
    - gradients: find edge-lik regions in the x and y direction
    - Canny edge detection: noise reduction (blurring), gradient (Sobel kernel in horizontal and vertical direction)


Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain
    - Edge detection: mathematical methods to find points in an image where the brightness of pixel intensities changes distinctly


"""
import numpy as np
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    # preprocessing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", image)

    #laplacian to compute gradient magnitude
    lap = cv2.Laplacian(image, cv2.CV_64F)
        # why 64-bit float --> 8-bit unsigned cannot represent negative numbers
            # black-to-white is a positive slope
            # white-to-black is a negative slope
            # without 64-bit we miss white-to-black transitions
    lap = np.uint8(np.absolute(lap))#
        # absolute to convert back to 8-bit - otherwise cv clips negative numbers at 0
    cv2.imshow("LoG", lap)

    cv2.waitKey(0)

    # Sobel operatator
    sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)# vertical gradients
    sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)# horizontal gradients

    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))

    sobelCombined = cv2.bitwise_or(sobelX, sobelY)

    cv2.imshow("Sobel X", sobelX)
    cv2.imshow("Sobel Y", sobelY)
    cv2.imshow("Sobel Combined", sobelCombined)
    cv2.waitKey(0)

if __name__=="__main__":
    main()