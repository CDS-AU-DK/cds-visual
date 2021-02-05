#Import your libraries and modules here
import os
import numpy as np
import cv2 

# Then define any functions you'll use
def translate(image, x, y):
    # Define translation matrix
    M = np.float64([[1, 0, x], 
                   [0, 1, y]])
    # Perform translation on our chosen image
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    # Return the translated image
    return shifted

# Then define a main() function
def main():
    """
    In a function called main(), you should include the 'core logic' or
    your script.
    """
    return

# Declare namespace - we'll go over this more
if __name__=="__main__":
    main()