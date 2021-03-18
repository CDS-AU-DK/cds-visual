#!/usr/bin/python
"""
Multilayered feedforward neural network
"""
# import the necessary packages
import numpy as np

class NeuralNetwork:
    def __init__(self, layers, alpha=.1):
        # init list of W matrices, store architecture and learning rate
        self.W = list()
        self.layers = layers
        self.alpha = alpha
        # loop from index of first layer, stop before last two layers
        for i in np.arange(0, len(layers) - 2):
            # random init w connecting nodes in each layer
            # add extra node for trainable bias
            w = np.random.randn(layers[i] + 1, layers[i + 1] + 1)
            self.W.append(w / np.sqrt(layers[i]))
        
        # for the last two layer the input conenctions need a bias term, but not the output
        w = np.random.randn(layers[-2] + 1, layers[-1]) 
        self.W.append(w / np.sqrt(layers[-2]))
    
    def __repr__(self):
        # construct & return string of neural network architecture
        return "NeuralNetwork: {}".format("-".join(str(l) for l in self.layers))
    
    def sigmoid(self, x):
        # activation function
        return 1.0 / (1 + np.exp(-x))

    def sigmoid_deriv(self, x):
        # derivate of the sigmoid activation function, assuming x has been passed through 
        # said function
        return x * (1 - x)
    
    def fit(self, X, y, epochs=1000, displayUpdate=100):
        # insert trainable bias column
        X = np.c_[X, np.ones((X.shape[0]))]

        # loop over epochs
        for epoch in np.arange(0, epochs):
            # loop over individual training points
            for (x, target) in zip(X, y):
                self.fit_partial(x, target)
            
            # check diaplay
            if epoch == 0 or (epoch + 1) % displayUpdate == 0:
                loss = self.calculate_loss(X, y)
                print("[INFO] epoch={}, loss={:.7f}".format(epoch + 1, loss))
            
    def fit_partial(self, x, y):
        # construct list of output activations for each layer
        # first activation is just the input
        A = [np.atleast_2d(x)]# A-ctivation list

        # FEEDFORWARD
        # loop through layers in network on forward pass
        for layer in np.arange(0, len(self.W)):
            # feedforward activation at the current layers as dot product
            # between activation and weight matrix
            # > net input to current layer
            net = A[layer].dot(self.W[layer])

            # compute net output
            out = self.sigmoid(net)

            # append to activation list
            A.append(out)

        # BACKPROPAGATION
        # first phase of backpropagation is to compute the
        # difference between our *prediction* (the final output
        # activation in the activation list) and the true target value
        error = A[-1] - y

        # apply chain rule and build list of deltas D; the first entry in deltas
        # is the eror of the output layer time the derivative of the activation function
        # for the output value
        D = [error * self.sigmoid_deriv(A[-1])]

        # loop in reverse order using the chain rule for each layer
        for layer in np.arange(len(A) - 2, 0, -1):
            # the delta for the current layer is equal to the delate of the 
            # previous layer dotted with the weight matrix of the current layer,
            # followed by multiplying the delta by the derivative of the nonlinear
            # activation for the activations of the current layer
            delta = D[-1].dot(self.W[layer].T)
            delta = delta * self.sigmoid_deriv(A[layer])
            D.append(delta)

        # reverse order of deltas for use in forward pass during weight update
        D = D[::-1]

        # WEIGHT UPDATE PHASE
        # forward pass, loop over layers
        for layer in np.arange(0, len(self.W)):
            # update weights by taking the dot product of the layer activations
            # with the respective deltas, then multiplying this value by the 
            # learning rate and add weight matrix
            # > actual learning phase
            self.W[layer] += -self.alpha * A[layer].T.dot(D[layer])

    def predict(self, X, addBias=True):
        # init output prediction as input features to forward propagate
        # through the network
        p = np.atleast_2d(X)

        # check if bias column should be added
        if addBias:
            p = np.c_[p, np.ones((p.shape[0]))]
        
        # forward pass over layers
        for layer in np.arange(0, len(self.W)):
            # compute output predictions as dot product of activation value p
            # and the weight matrix associated with the current layer, then
            # passing the value through a nonlinear activation function
            p = self.sigmoid(np.dot(p, self.W[layer]))
        
        # return predicted value
        return p
    
    def calculate_loss(self, X, targets):
        # make predictions for input and compute loss
        targets = np.atleast_2d(targets)
        predictions = self.predict(X, addBias=False)
        loss = .5 * np.sum((predictions - targets) ** 2)

        return loss