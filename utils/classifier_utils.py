#!/usr/bin/env python
"""
tools for teaching image classification with sklearn

"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_sample(X, y, classes, samples_per_class):
    """
    Plots a grid of samples for each class
    
    data: the data to be plotted
    classes: list of all classes
    samples_per_class: number of samples to show
    """
    nclasses = len(classes)
    figure = plt.figure(figsize=(nclasses*2,(1+samples_per_class*2)))

    # for each value in classes
    for idx_cls, cls in enumerate(classes):
        # pick some at random to plot
        idxs = np.flatnonzero(y == cls)
        idxs = np.random.choice(idxs, samples_per_class, replace=False)
        # plot on a grid for comparison
        for i, idx in enumerate(idxs):
            plt_idx = i * nclasses + idx_cls + 1
            p = plt.subplot(samples_per_class, nclasses, plt_idx);
            p = sns.heatmap(np.reshape(X[idx], (28,28)), cmap=plt.cm.gray, 
                            xticklabels=False, yticklabels=False, cbar=False)
            p = plt.axis('off')
    
    return None

def plot_coefs(coefficients, nclasses):
    """
    Plot the coefficients for each label
    
    coefficients: output from clf.coef_
    nclasses: total number of possible classes
    """
    scale = np.max(np.abs(coefficients))

    p = plt.figure(figsize=(25, 5))

    for i in range(nclasses):
        p = plt.subplot(1, nclasses, i + 1)
        p = plt.imshow(coefficients[i].reshape(28, 28),
                      cmap=plt.cm.RdBu, vmin=-scale, vmax=scale)
        p = plt.axis('off')
        p = plt.title('Class %i' % i)
        
    return None

def plot_individual(X, y, sample_idx):
    """
    Show individual data point
    
    X: data source
    y: label source
    sample_idx: index of sample to be plotted 
    """
    #plotting image
    plt.imshow(X[sample_idx].reshape(28,28), cmap='gray')
    plt.title(f'Label: {y[sample_idx]}\n')
    plt.axis('off')
    
    return None

def plot_probs(X, sample_idx, model, classes):
    """
    Plot probability distribution for individual test case
    
    X: input data source
    sample_idx: the data point to study
    model: trained classifier model
    classes: predefined list of classes
    """
    nclasses = len(classes)
    z = [model.intercept_[k] + np.dot(model.coef_[k], X[sample_idx]) for k in range(nclasses)]
    #conditional probability
    exps = [np.exp(z[k])/1+np.exp(z[k]) for k in range(10)]
    exps_sum = np.sum(exps)
    probs = exps/exps_sum
    #plot
    sns.barplot(x=classes, y=probs);
    plt.ylabel("Probability");
    plt.xlabel("Class");
    
    #predictied label
    idx_cls = np.argmax(probs)
    print(f"I think that this is class {classes[idx_cls]}")
    
    return None

def plot_cm(y_test, y_pred, normalized:bool):
    """
    Plot confusion matrix
    """
    if normalized == False:
        cm = pd.crosstab(y_test, y_pred, 
                            rownames=['Actual'], colnames=['Predicted'])
        p = plt.figure(figsize=(10,10));
        p = sns.heatmap(cm, annot=True, fmt="d", cbar=False)
    elif normalized == True:
        cm = pd.crosstab(y_test, y_pred, 
                               rownames=['Actual'], colnames=['Predicted'], normalize='index')
        p = plt.figure(figsize=(10,10));
        p = sns.heatmap(cm, annot=True, fmt=".2f", cbar=False)
        
def predict_unseen(image, model, classes):
    """
    Predict the category of unseen data, show probabilities 
    
    image: unseen data
    model: trained model
    classes: list of possible classes
    """
    # Reshape array
    test_probs = model.predict_proba(image.reshape(1,784))
    # plot prediction
    sns.barplot(x=classes, y=test_probs.squeeze());
    plt.ylabel("Probability");
    plt.xlabel("Class")
    
    #predictied label
    idx_cls = np.argmax(test_probs)
    print(f"I think that this is class {classes[idx_cls]}")
    
    return None

def prediction_coefficients(image, model, classes):
    # get number of classes
    nclasses = len(classes)
    # scale the output based on max values
    scale = np.max(np.abs(model.coef_))

    p = plt.figure(figsize=(25, 5));
    
    for i in range(nclasses):
        p = plt.subplot(2, nclasses, i + 1)
        p = plt.imshow(model.coef_[i].reshape(28, 28),
                      cmap=plt.cm.RdBu, vmin=-scale, vmax=scale);
        p = plt.title('Class %i' % i);
        p = plt.axis('off')

    for i in range(nclasses):
        p = plt.subplot(2, nclasses, nclasses + i + 1)
        p = plt.imshow(image*model.coef_[i].reshape(28, 28),
                      cmap=plt.cm.RdBu, vmin=-scale/2, vmax=scale/2);
        # note: you can adjust the scaling factor if necessary,
        # to make the visualization easier to understand
        p = plt.axis('off')
        
    return None
    
if __name__=="__main__":
    pass