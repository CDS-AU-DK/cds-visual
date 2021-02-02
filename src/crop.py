#!/usr/bin/env python
"""
exemplify cropping, 

Parameters

Usage

Example
    $ python crop.py --image ../img/trex.png

## Explain
    - array slicing to extract rectangular region
"""
import numpy as np
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    cropped = image[30:120, 240:335]# lice y coordinate 30:120 & x coordinate 240 to 335
    cv2.imshow("T-Rex Face", cropped)

    cv2.waitKey(0)

if __name__=="__main__":
    main()