#!/usr/bin/env python
"""

Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain

"""
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)
    plot_histogram(image, "Histogram for Original Image")
    plt.savefig("../fig/unmasked_histogram.png")

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
    cv2.imshow("Mask", mask)

    masked = cv2.bitwise_and(image, image, mask = mask)
    cv2.imshow("Applying the Mask", masked)

    plot_histogram(image, "Histogram for Masked Image", mask = mask)

    plt.savefig("../fig/masked_histogram.png")

    cv2.waitKey(0)

if __name__=="__main__":
    main()