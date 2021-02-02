#!/usr/bin/env python
"""
exemplify histogram equalization to improve contrast
    - unrealistic effects in pictures, improves contrast for medical imaging

Parameters

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
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    eq = cv2.equalizeHist(image)

    cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
    cv2.waitKey(0)

if __name__=="__main__":
    main()