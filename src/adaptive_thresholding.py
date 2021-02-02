#!/usr/bin/env python
"""
Exemplify adaptive thresholding to avoid one threshold value that is manually determined
--> considers small neighbors of pixels and then finds an optimal threshold value T for each neighbor.


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
    # preprocessing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5,5), 0)
    cv2.imshow("Image", image)

    thresh = cv2.adaptiveThreshold(blurred, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C,# method for computing threshold (mean of neighborhood) 
        cv2.THRESH_BINARY_INV,# method fo thresholding 
        11,# neighborhood pixel size
        4# parameter C subtracted from the mean to fine-tune thresholding
        )
    cv2.imshow("Mean Thresh", thresh)
    
    thresh = cv2.adaptiveThreshold(blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        15,
        3
        )
    cv2.imshow("Gaussian Thresh", thresh)

    cv2.waitKey(0)

if __name__=="__main__":
    main()