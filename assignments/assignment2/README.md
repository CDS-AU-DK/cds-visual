# Assignment 2 - Classification benchmarks with Logistic Regression and Neural Networks

For this assignment, we'll be writing scripts which classify the ```Cifar10``` dataset. You can read more about this dataset [here](https://www.cs.toronto.edu/~kriz/cifar.html)

The data already has a train/test split and can be loaded in the following way:

```python
from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
```

You should write code which does the following:

- Load the Cifar10 dataset
- Preprocess the data (e.g. greyscale, reshape)
- Train a classifier on the data
    - A logistic regression classifier *and* a neural network classifier
- Save a classification report
- Save a plot of the loss curve during training

You should write **two scripts** for this assignment one script which does this for a logistic regression classifier **and** one which does it for a neural network classifier. In both cases, you should use the machine learning tools available via ```scikit-learn``` to evaluate model performance.

## Tips

- The Cifar10 dataset you download does not have explict label names but instead has numbers from 0-9. You'll need to make a list of labels based on the object names - you can find these on the website.
- You should structure your project by having scripts saved in a folder called ```src```, and have a folder called ```out``` where you save the classification reports.

## Purpose

- To ensure that you can use ```scikit-learn``` to build simple benchmark classifiers on image classification data
- To demonstrate that you can build reproducible pipelines for machine learning projects
- To make sure that you can structure repos appropriately
