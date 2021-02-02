#!/usr/bin/env python
"""
exemplify translation - shifting rgof an image along the x and y axis - with openCV


Parameters

Usage

Example
    $ python translation.py --image ../img/trex.png

## Explain
    - Functions
    - Translation matrix: 
    - Variable type: float

"""
import argparse
import numpy as np
import cv2
import imutils# library to be created

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)
    
    # translation matrix: many pixels to the left or right, and up or down.
    M = np.float32([[1, 0, 25], [0, 1, 50]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Down and Right", shifted)

    M = np.float32([[1, 0, -50], [0,1,-90]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Up and Left", shifted)

    # shifting with a function
    shifted = imutils.translate(image, 0, 100)
    cv2.imshow("Shifted Down", shifted)
    cv2.waitKey(0)   

if __name__=="__main__":
    main()