#!/usr/bin/env python
"""
exemplify rotation by some angle $\theta$

Parameters

Usage

Example
    $ python rotate.py --image ../img/trex.png

## Explain


"""
import numpy as np
import argparse
import imutils
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    (h, w) = image.shape[:2]
    center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, 45, 1.0)# center, \theta, scale
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)

    M = cv2.getRotationMatrix2D(center, -90, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h))
    cv2.imshow("Rotated by -90 Degrees", rotated)
    
    # function
    rotated = imutils.rotate(image, 180)
    cv2.imshow("Rotated by 180 Degrees", rotated)

    cv2.waitKey(0)

if __name__=="__main__":
    main()