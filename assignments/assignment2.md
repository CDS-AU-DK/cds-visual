# Assignment 2 - Image classifier benchmark scripts

In the last two classes, you've seen how to train a model that can be used to make classification predictions on image data. So far, we've seen two different approaches. The first approach is a simple logistic regression classifier; the second uses a (very inefficient!) neural network class written in ```numpy```. 

In class, we saw how these classifiers worked through the use of Notebooks in Jupyter Lab. However, as we spoke about in class, these Notebooks are not the best way to use and share code. Instead, what we want is a script that can be run and which then produces the outputs with minimal input from the user.

For this assignment, you will take the classifier pipelines we covered in lecture 7 and turn them into *two separate ```.py``` scripts*. Your code should do the following:

- One script should be called ```logistic_regression.py``` and should do the following:
  - Load either the **MNIST_784** data or the **CIFAR_10** data
  - Train a Logistic Regression model using ```scikit-learn```
  - Print the classification report to the terminal **and** save the classification report to ```out/lr_report.txt```
- Another scripts should be called ```nn_classifier.py``` and should do the following:
  - Load either the **MNIST_784** data or the **CIFAR_10** data
  - Train a Neural Network model using the premade module in ```neuralnetwork.py```
  - Print output to the terminal during training showing epochs and loss
  - Print the classification report to the terminal **and** save the classification report to ```out/nn_report.txt```

## Tips and pointers - READ THIS
- You are welcome to work on this and submit as a group, even though it says Individual Assignment
- Structure your repo in the way that I introduced: ```in```, ```out```, ```src```, ```README.md```.

## Bonus tasks
- Use ```argparse()``` so that the scripts use either **MNIST_784** or **CIFAR_10** based on some input from the user on the command line
- Use ```argparse()``` to allow users to define the number and size of the layers in the neural network classifier.
- Write the script in such a way that it can take either **MNIST_784** or **CIFAR_10** or **any data that the user wants to classify**
  - You can determine how the user data should be structured, by saying that it already has to be pre-processed or feature extracted.

## Goals and outcomes
- The purpose of this assignment is to demonstrate that you know how to create ```.py``` scripts with simple classifiers that can act as benchmarks for future reasearch
- After completing this assignment, you will have a couple of scripts which could be re-written and reused on separate data