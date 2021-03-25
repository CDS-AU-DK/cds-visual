#!/usr/bin/python
"""
Train LogisticRegression on mnist (sample) as baseline
"""
import sys,os
sys.path.append(os.getcwd())
import argparse
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
#from sklearn import datasets, metrics
from sklearn.datasets import fetch_openml

def main():
    # Argument parser
    ap = argparse.ArgumentParser()
    # CLI parameters
    ap.add_argument("-s", "--split", required=True, help="Test split percentage")
    # Parse input arguments
    args = vars(ap.parse_args())
    # Parse train-test split value
    split = float(args["split"])
    
    # load data and apply min/max scaling
    # each image is 8x8 pixels grayscale
    print("[INFO] loading MNIST (sample) dataset")
    #digits = datasets.load_digits()
    data, labels = fetch_openml('mnist_784', version=1, return_X_y=True)
    
    # to data
        #data = digits.data.astype("float")
    data = data.astype("float")
    data = (data - data.min())/(data.max() - data.min())
    print("[INFO] samples: {}, dim: {}".format(data.shape[0], data.shape[1]))

    # split data
    (trainX, testX, trainY, testY) = train_test_split(data, 
                                                      labels, 
                                                      test_size=split)

    # train network
    print("[INFO] training classifier...")
    clf = LogisticRegression(penalty='none', 
                             tol=0.1, 
                             solver='saga',
                             verbose=True,
                             multi_class='multinomial').fit(trainX, trainY)

    # evaluate network
    print(["[INFO] evaluating network..."])
    predictions = clf.predict(testX)
    #predictions = predictions.argmax(axis=1)
    cm = classification_report(testY, predictions)
    print(cm)

if __name__=="__main__":
    main()
