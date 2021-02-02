#!/usr/bin/env python
"""
Load, display, and write image to jpg

Parameters:
    image: str <path-to-image>
Usage:
    load_display_save.py --image <path-to-image>
Example:
    $ python load_display_save.py --image ../img/trex.png
"""
import argparse
import os
import cv2

def main():
    ap = argparse.ArgumentParser()
    # parameters
    ap.add_argument("-i", "--image", required=True, help="Path to image file")
    args = vars(ap.parse_args())
    # image object
    image = cv2.imread(args["image"])
    # dimensions
    print("[INFO] width: {} pixels".format(image.shape[1]))
    print("[INFO] height: {} pixels".format(image.shape[0]))
    print("[INFO] channels: {}".format(image.shape[2]))
    # show
    cv2.imshow("image", image)
    cv2.waitKey(0)
    # write
    (fpath, fname) = os.path.split(args["image"])
    fout = os.path.join(fpath, "newimage.jpg")
    cv2.imwrite(fout, image)

if __name__=="__main__":
    main()