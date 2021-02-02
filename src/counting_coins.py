#!/usr/bin/env python
"""
find contours/curves in an image, a contour is a curve of points, with no
gaps in the curve. Contours are extremely useful for such
things as shape approximation and analysis.
 


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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11,11), 0)
    cv2.imshow("Image", image)

    edged = cv2.Canny(blurred, 30, 150)
    cv2.imshow("Edges", edged)

    (cnts, _) = cv2.findContours(edged.copy(), 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE
        )
    # image is destroyed, therefore .copy method
    # returns a 2-tuple, image, contours and hierarchy of contours
    # param1: type of contours - retrieve only the outermost contours/EXTERNAL
        # RETR_LIST will return all contours; RETR_COMP and RETR_TREE can return hierarchy
    # param2: how to approximate contours; simple compress horizontal, vertical and diagonal - save computation and memory 
    print("[INFO] Detected {} coins in this image".format(len(cnts)))

    coins = image.copy()
    cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
    # param2: list of contours
    # param3: which contours to draw, -1 all
    # param4: color of contour
    # param5: thickness
    cv2.imshow("Coins", coins)
    cv2.waitKey(0)

    # crop individual coins
    for (i, c) in enumerate(cnts):
        (x, y, w, h) = cv2.boundingRect(c)# finds enclosing region of contour

        print("[INFO] #{}".format(i + 1))
        coin = image[y:y + h, x:x + w]# slice/crop region
        cv2.imshow("Coin", coin)

        mask = np.zeros(image.shape[:2], dtype="uint8")
        ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)# fits circle to contour

        cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)# create mask
        mask = mask[y:y + h, x:x + w]# slice/crop mask

        cv2.imshow("Masked coin", cv2.bitwise_and(coin, coin, mask = mask))
        # remove background
        cv2.waitKey(0)


if __name__=="__main__":
    main()