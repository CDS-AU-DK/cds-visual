#!/home/knielbo/virtenvs/cv/bin/python
"""
Implementation of convolutions
"""
from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2


def convolve(image, K):
    # grab spatial dimensions of image and kernel
    (iH, iW) = image.shape[:2]
    (kH, kW) = K.shape[:2]

    # allocate memory for the output image
    # create padding on the borders in order to keep the spatial size constant
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float")
    
    # loop over input image, "sliding" the kernel across
    # each (x, y)-coordinate from left-to-right and top-to-bottom
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # extract ROI by extracting the center of the region of
            # the current (x, y)-coordinates dimensions
            roi = image[y-pad : y+pad+1, x-pad : x+pad+1]

            # perform the convolution by taking the element-wise
            # multiplication between the ROI and the kernel, then
            # summing the matrix
            k = (roi * K).sum()

            # store convolved value in the output (x, y)-coordinate
            # of the output image
            output[y-pad, x-pad] = k

    # rescale output to [0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    args = vars(ap.parse_args())

    # construct average blurring kernels to smooth an image
    smallBlur = np.ones((7, 7), dtype="float") * (1. / (7 * 7))
    largeBlur = np.ones((21, 21), dtype="float") * (1. / (21 * 21))

    # sharpening filter
    sharpen = np.array((
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]), dtype="int")
    # Laplacian kernel to detect edge-like regions
    laplacian = np.array((
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]), dtype="int")
    # Sobel kernel for horizontal edge-like regions
    sobelX = np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")
    # Sobel kernel for vertical edge-like regions
    sobelY = np.array((
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]), dtype="int")
    # emboss kernel, each pixel of an image is replaced either by a highlight or 
    # a shadow, depending on light/dark boundaries on the original image
    emboss = np.array((
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]), dtype="int")

    # kernel bank
    kernelBank = (
        ("small_blur", smallBlur),
        ("large_blur", largeBlur),
        ("sharpen", sharpen),
        ("laplacian", laplacian),
        ("sobel_x", sobelX),
        ("sobel_y", sobelY),
        ("emboss", emboss)
        )
    
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # loop over kernels in kernel bank
    for (kernelName, K) in kernelBank:
        # apply kernel to grayscale image using both
        # custom convolve func and OpenCV's filter2D fund
        print("[INFO] applying {} kernel".format(kernelName))
        convolveOutput = convolve(gray, K)
        opencvOutput = cv2.filter2D(gray, -1, K)

        # show images
        cv2.imshow("original", gray)
        cv2.imshow("{} - concolve".format(kernelName), convolveOutput)
        cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__=="__main__":
    main()