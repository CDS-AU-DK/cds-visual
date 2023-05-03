# Session 10 - More on image embeddings

## Overview

Last week we saw how VGG16 can be used as a feature extractor to create what are called *image embeddings*. These image embeddings are dense numerical representations of our images, created using the pre-trained weights from VGG16. 

We used these embeddings last week as the input layer to a classification network, and found that we could reach an average F1 across ```CIFAR-10``` of around about 0.52, a 0.3 increase over our first attempt which made the image greyscale and flattened pixel values to a single 1D input. That's cool!

This week, we'll see how we can use the image embeddings themselves to explore data, by building a more sophisticated image search algorithm than the one we made previously using colour historams. We'll also see some simple ways of performing basic style transfer, which leads us to our final topic next week on *generative image models*.

We'll also have some time to continue work on [Assignement 3](https://classroom.github.com/a/Aj7Sf-j_)

## Tasks
- Using VGG16 to extract image embeddings
- K-Nearest Neighbours in ```scikit-learn```
- A simple example of style transfer
- Continuing with [Assignment 3](https://classroom.github.com/a/Aj7Sf-j_)
