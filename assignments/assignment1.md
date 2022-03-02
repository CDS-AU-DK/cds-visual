# Assignment 1 - Image search

In the last few weeks, we've seen how images can be deconstructed into the three colour channels which they comprise (RGB). We saw that, in some ways, the colour histogram of an image is its "colour fingerprint". We also saw that images can be compared for similarity of their colour histograms, allowing us to find which images are most like each other in terms of their colour.

For this assignment, you will write a small Python program to compare image histograms quantitively using Open-CV and the other image processing tools you've already encountered. Your script should do the following:

- Take a user-defined image from the folder
- Calculate the "distance" between the colour histogram of that image and all of the others.
- Find which 3 image are most "similar" to the target image.
- Save an image which shows the target image, the three most similar, and the calculated distance score.
- Save a CSV which has one column for the filename and three columns showing the filenames of the closest images in descending order

For this assignment, you should create a private Github repository and add me as a collaborator. When submitting via Brightspace, simply send the link to the repository; I will provide feedback and comments via Github's built in functionality.

## Tips and pointers
- You are welcome to work on this and submit as a group, even though it says Individual Assignment
- Try to provide a README file which outlines the contents of the repository
- For your dataset, you should use the novels in the shared data folder for CDS-VIS, under _flowers_
- Calculate distance using the __cv2.HISTCMP_CHISQR__ function in Open-CV
- Remember to _normalize_ your images using something like __MinMax__

## Bonus tasks
- Create a program which does this for the whole dataset, creating a CSV with one column showing the file name for each image and three other columns showing the most similar images

## Goals and outcomes
- The goal of this assignment is to demonstrate that you have a good understanding of how to use simple image processing techniques to extract valuable information from image data
- By the end of this assignment, you will have a simple tool for performing _image search_ on a dataset of images, finding which images are most similar to one another