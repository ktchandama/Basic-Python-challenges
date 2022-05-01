#Here, we will write a function neural_network, which will apply a neural network operation with 2 inputs and 1 output and a given weight matrix.
#import numpy as np
def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    z = np.tanh(weights.T.dot(inputs))
    
    return z
    raise NotImplementedError
    

 
#Let's start with writing a scalar function scalar_function, which will apply the following operation with input x and y.
#The function outputs x*y if x<=y and x/y else
def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if x <= y :
        f = x*y
    else :
        f = x/y
    return f
    raise NotImplementedError
