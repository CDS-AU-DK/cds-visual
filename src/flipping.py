#!/usr/bin/env python
"""
exemplify flipping, flip an image around either the x or y axis, or even both

Parameters

Usage

Example
    $ python flipping.py --image ../img/trex.png

## Explain
"""
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    flipped = cv2.flip(image, 1)
    cv2.imshow("Flipped Horizontally", flipped)

    flipped = cv2.flip(image, 0)
    cv2.imshow("Flipped Vertically", flipped)

    flipped = cv2.flip(image, -1)
    cv2.imshow("Flipped Horizontally & Vertically", flipped)

    cv2.waitKey(0)

if __name__=="__main__":
    main()