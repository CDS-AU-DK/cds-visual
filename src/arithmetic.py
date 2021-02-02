#!/usr/bin/env python
"""
solutions to arithmetic operations in limited numerical spaces, e.g., 8-bit unsigned integer
a) cv2: clipping at max/min value
b) numpy: modulo arithmetic and 'wrap around'

Parameters

Usage

Example
    $ python arithmetic.py --image ../img/trex.png

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

    # exemplify arithmetic with 8bit unsigned integers
    ## clippling values at extrema
    print("[INFO] max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
    print("[INFO] min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
    ## wrap around
    print("[INFO] wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
    print("[INFO] wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

    # arithmetic operations on images
    ## addition
    M = np.ones(image.shape, dtype="uint8") * 100
    added = cv2.add(image, M)
    cv2.imshow("Added", added)

    ## subtraction
    M = np.ones(image.shape, dtype="uint8") * 50
    subtracted = cv2.subtract(image, M)
    cv2.imshow("Subtracted", subtracted)

    cv2.waitKey(0)

if __name__=="__main__":
    main()