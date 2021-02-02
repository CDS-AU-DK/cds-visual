#!/usr/bin/env python
"""
Exemplify masking functionality with bitwise operations

Parameters

Usage

Example
    $ python masking.py --image ../img/<filename>.png

## Explain
    - key point of masks is that they allow us to focus our computation only on regions of the image that interests us.


"""
import numpy as np
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    # rectangular mask for sky & trees
    mask = np.zeros(image.shape[:2], dtype="uint8")
    (cX, cY) = (image.shape[1]//2, image.shape[0]//2)
    cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
    cv2.imshow("Mask", mask)

    masked = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)

    # circular mask for sky and trees
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask, (cX, cY), 100, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Mask Applied to Image", masked)
    cv2.waitKey(0)



if __name__=="__main__":
    main()