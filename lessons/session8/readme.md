# Session 8 - Convolutional Neural Networks with TensorFlow

## Overview

Last week, we look in more depth at how neural networks learn from data. However, even if the maths is challenging, the networks we've been looking at so far are fairly simple in construction. We have a single 1D input layer, some hidden layers with a logistic or ReLU activation function, and an output that gives us a probability distribution over all the possible classes.

This is fine, but the problem is that we are working with image data which comprises three distinct colour channels. To use the technical terms we saw last week, images are tensors of rank 3. When we make them greyscale and flatten down to 1 dimension, we're losing a *lot* of information about how images are structed.

In the code along session, we'll see how we can use ```TensorFlow``` to create convolutional neural networks which can work with image data in full colour, without the need to make greyscale.

## Tasks
- Working through notebook
- Some coding tasks