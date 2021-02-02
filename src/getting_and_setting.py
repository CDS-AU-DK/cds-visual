#!/usr/bin/env python
"""
Load image, grab and manipulate image region

Parameters:
    image: str <path-to-image>
Usage:
    getting_and_setting.py --image <path-to-image>
Example:
    $ python getting_and_setting.py --image ../img/trex.png

## Explain

- RGB and BGR triplets: BGR is the horse's ass in OpenCV." OpenCV reads in images in 
BGR format (instead of RGB) because when OpenCV was first being developed, 
BGR color format was popular among camera manufacturers and image software. 

- slicing arrays


## Task
Manipulate color of pixel region
Move pixel region
Loop over BGR triplet of pixel region
"""
import argparse
import os
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    # image object
    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)
    # OpenCV stores RGB pixels in reverse tuples, so BGR
    (b, g, r) = image[0, 0]
    print("[INFO] pixels at (0, 0) - Red: {}, Green {}, Blue: {}".format(r,g,b))
    # manipulate image color for pixel
    image[0, 0] = (0, 0, 255)
    (b, g, r) = image[0, 0]
    print("[INFO] pixels at (0, 0) - Red: {}, Green {}, Blue: {}".format(r,g,b))
    # grab 100x100 pixel region
    corner = image[0:100, 0:100]
    cv2.imshow("Corner", corner)
    ## change color of 100x100 pixel region
    image[0:100,0:100] = (0, 0, 255)
    cv2.imshow("Updated", image)
    # close image
    cv2.waitKey(0)

if __name__=="__main__":
    main()