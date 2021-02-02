#!/usr/bin/env python
"""
exemplify grayscale color histogram

Parameters

Usage

Example
    $ python <scriptname>.py --image ../img/<filename>.png

## Explain

"""
import matplotlib.pyplot as plt
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", image)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    M = [image, hist]
    fig, ax = plt.subplots(1, 2, figsize=(10,4))
    for(i, img) in enumerate(M):
        if i == 0:
            ax[i].imshow(img, cmap="gray")
        else:
            ax[i].plot(img, c="k")
            ax[i].set_title("Grayscale Histogram")
            ax[i].set_xlabel("Bins")
            ax[i].set_ylabel("# of Pixels")
            ax[i].set_xlim([0, 256])
    plt.savefig("../fig/grayscale_histogram.png")
    cv2.waitKey(0)

if __name__=="__main__":
    main()