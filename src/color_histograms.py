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

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    image = cv2.imread(args["image"])
    #cv2.imshow("Original", image)

    chans = cv2.split(image)
    colors = ("b", "g", "r")

    fig, ax = plt.subplots(1,2, figsize=(10,4))
    ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax[1].set_title("’Flattened’ Color Histogram")
    ax[1].set_xlabel("bins")
    ax[1].set_ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        ax[1].plot(hist, color=color)
        ax[1].set_xlim([0, 256])

    plt.savefig("../fig/color_histogram.png")

    # compare channels incrementally
    fig = plt.figure(dpi=300, figsize=(12,4))
    
    ax = fig.add_subplot(131)
    hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0 ,256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for G and B")
    ax.set_ylabel("G")
    ax.set_xlabel("B")
    plt.colorbar(p)

    ax = fig.add_subplot(132)
    hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0 ,256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for G and R")
    ax.set_ylabel("G")
    ax.set_xlabel("R")
    plt.colorbar(p)

    ax = fig.add_subplot(133)
    hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0 ,256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for B and R")
    ax.set_ylabel("B")
    ax.set_xlabel("R")
    plt.colorbar(p)

    plt.savefig("../fig/histogram_2d.png")

    print("[INFO] 2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

if __name__=="__main__":
    main()