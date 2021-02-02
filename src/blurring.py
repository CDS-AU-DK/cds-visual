#!/usr/bin/env python
"""
Exemplify blurring

Each pixel in the image is mixed in with its surrounding pixel intensities. 
The 'mixture' of pixels in a neighborhood becomes our blurred pixel.

Purpose:
    - reduce noise and detail in an image at the cost of edges
    - bilateral keeps edges

Techniques to exemplify:
    - Averaging: [Convolution Kernel] define a k × k sliding window on top of our image, where k is always an odd number. 
    - Gaussian: similar to average blurring, but with a weighted mean,  where neighborhood pixels that are closer to the central pixel contribute more weight to the average
    - Median: (removal of salt and pepper noise) median of k x k neighborhood
    - Bilateral: (keep edges) using two gaussian distributions, The first Gaussian function only considers spatial neighbors, that is, pixels that appear close together in the ( x, y ) coordinate space of the image. The second Gaussian then
        models the pixel intensity of the neighborhood, ensuring that only pixels with similar intensity are included in the actual computation of the blur.



applications:
- preprocessing: thresholding and edge detection, perform better if the image is first smoothed or blurred.


Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain
    - Convolution Kernels
    - hstack(): horizontal stack of images


"""
import numpy as np
import argparse
import cv2
from numpy.core.shape_base import hstack

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    # averaging
    blurred = np.hstack([
        cv2.blur(image, (3, 3)),
        cv2.blur(image, (5, 5)),
        cv2.blur(image, (7, 7))]
        )
    cv2.imshow("Averaged", blurred)

    cv2.waitKey(0)

    # gaussian, third parameter is \sigma = 0, then computed for kernel size
    blurred = np.hstack([
        cv2.GaussianBlur(image, (3, 3), 0),
        cv2.GaussianBlur(image, (5, 5), 0),
        cv2.GaussianBlur(image, (7, 7), 0)]
        )
    cv2.imshow("Gaussian", blurred)
    cv2.waitKey(0)

    # median, does not "invent" pixel values, kernel removes details and noise
    blurred = np.hstack([
        cv2.medianBlur(image, 3),
        cv2.medianBlur(image, 5),
        cv2.medianBlur(image, 7)]
        )
    cv2.imshow("Median", blurred)
    cv2.waitKey(0)

    # bilateral, keeps edges vai 2 gaussian, only smooth similar intensity, slow algo
    blurred = np.hstack([
        cv2.bilateralFilter(image, 3, 21, 21),
        cv2.bilateralFilter(image, 7, 31, 31),
        cv2.bilateralFilter(image, 9, 41, 41)
    ])
    cv2.imshow("Bilateral", blurred)
    cv2.waitKey(0)
    # second argument: diameter of pixel neighborhood
    # third argument: color \sigma (number of colors to consider)
    # fourth argument: space \sigma (number of pixel to consider)

if __name__=="__main__":
    main()