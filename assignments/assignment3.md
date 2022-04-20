# Assignment 3 - Transfer learning + CNN classification

In the previous assignment, you built simple set of classifiers to work with the *CIFAR10* data set. Those classifiers were fairly simple, insofar as we just flattened the images into a 1D array of features and fed that into either a LogisticRegression Classifier or a fully-connected, feed-forward neural network. 

This approach - converting to grey scale, flattening images - means that we lose a lot of potentially meaningful information in the data. We've also seen, though, that *Convolutional Neural Networks* are specifically designed for working with image data, allowing us to retain more of the original image. Particularly deep, complex CNNs that have been pretrained on a huge amount of data can be used as a feature extraction tool, converting our images into dense vector representations. This process is known as *transfer learning*.

In this assignment, you are still going to work with the CIFAR10 dataset. However, this time, you are going to make build a classifier using transfer learning with a pretrained CNN like VGG16 for feature extraction. 

Your ```.py``` script should minimally do the following:

- Load the CIFAR10 dataset
- Use VGG16 to perform feature extraction
- Train a classifier 
- Save plots of the loss and accuracy 
- Save the classification report

## Tips and pointers - READ THIS
- You are welcome to work on this and submit as a group, even though it says Individual Assignment
- Structure your repo in the way that I introduced: ```in```, ```out```, ```src```, ```README.md```.

## Bonus tasks
- Use ```argparse()``` to allow users to define specific hyperparameters in the script.
  - This might include e.g. learning rate, batch size, etc
- The user should be able to define the names of the output plot and output classification report from the command line
  
## Goals and outcomes
- The purpose of this assignment is to show that you are able to use transfer learning in the context of image data, a state-of-the-art task in deep learning
- This assignment is also intended to increase your familiarity of working with ```Tensorflow/Keras```, and with building complex deep learning pipelines
- After completing this assignment, you will have the basic outline of a classification pipeline using transfer learning which can be adapted and modified for future tasks