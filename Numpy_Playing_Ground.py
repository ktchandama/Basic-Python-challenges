#Let's write a function called randomization that takes as input a positive integer n, and returns A, a random n x 1 Numpy array
#import numpy as np
def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = np.random.random(size=n).reshape(n,1)
    
    return A
    raise NotImplementedError
    
    
    #Let's now Write a function called operations that takes as input two positive integers h and w, makes two random matrices A and B, of size h x w, 
    #and returns A,B, and s, the sum of A and B
    def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    #Your code here
    A = np.random.random(size=(h,w))
    
    
    #Writing a function called norm that takes as input two Numpy column arrays A and B, adds them, and returns s, the L2 norm of their sum.
    def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    s = A + B
    
    return np.linalg.norm(s)
