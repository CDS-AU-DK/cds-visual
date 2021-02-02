#!/usr/bin/env python
"""
Edge detection with Canny edge detector which reduces noise (compared to Laplacian and Sobel)
Parameters
    -> create crisp and noise-less edge detection
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
    # preprocessing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Blurred", image)

    canny = cv2.Canny(image, 30, 150)
        # param2: threshold 1: any gradient value below is not an edge
        # param3: threshold 2: any gradient value above is an edge
        # thres 1 < value < thres 2 are classified as edge depending on how its intesities are connected
    cv2.imshow("Canny", canny)

    cv2.waitKey(0)

if __name__=="__main__":
    main()