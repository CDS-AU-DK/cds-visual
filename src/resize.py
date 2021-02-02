#!/usr/bin/env python
"""
exemplify rotation by some angle $\theta$

Parameters

Usage

Example
    $ python resize.py --image ../img/trex.png

## Explain
    - aspect ratio
    - conditionals in functions


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

    # width-based resizing
    ## fixing aspect ratio
    r = 150.0 / image.shape[1]# resize to 150 pixel width using ratio r
    dim = (150, int(image.shape[0] * r))# compute new height with ratio r
    ## resizing
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    ## INTER_AREA for interpolation method is algorithm for resizing
    cv2.imshow("Resized (Width)", resized)

    # height-based resizing
    r = 50.0 / image.shape[0]
    dim = (int(image.shape[1] * r), 50)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized (Height)", resized)


    resized = imutils.resize(image, height=600)
    cv2.imshow("Resized via Function", resized)

    cv2.waitKey(0)
    
if __name__=="__main__":
    main()