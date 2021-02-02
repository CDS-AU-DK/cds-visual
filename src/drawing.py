#!/usr/bin/env python
"""
exemplifies OpenCV's drawing functionality

Parameters

Usage

Example


## Explain

- Methods
    - line, rectangle, circle
    - namespace: cv2
- Loops
    - indentation
    - 
- Random number generatation
- Variable types
    - integers


## Tasks


"""
import numpy as np
import cv2


def main():
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    # draw lines
    green = (0, 255, 0)
    cv2.line(canvas, (0,0), (300, 300), green)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    ## width
    red = (0, 0, 255)
    cv2.line(canvas, (300, 0), (0,300), red, 3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    # draw rectangles
    cv2.rectangle(canvas, (10,10), (60, 60), green)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    ## width
    cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    ## filled in
    blue = (255, 0, 0)
    cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    # draw circles
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    ## data types, integer division
    (centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
    white = (255, 255, 255)
    ## loops and indentation
    for i in range(0, 175, 25):
        cv2.circle(canvas, (centerX, centerY), i, white)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

    # abstract drawing, explain random number capabilities
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    for i in range(0, 25):# 25 circles
        ## three variables; radius, color, pt/center
        radius = np.random.randint(5, high=200)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        pt = np.random.randint(0, high=300, size=(2,))

        cv2.circle(canvas, tuple(pt), radius, color, -1)
    
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)

if __name__=="__main__":
    main()