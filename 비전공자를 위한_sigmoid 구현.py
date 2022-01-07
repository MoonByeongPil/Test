import numpy as np
import math 

def Linear(x):
    return 2*x+4

def Sigmoid(x):
    return 1/(1+np.exp(-x))

def ReLU(x):
    return max(x,0)

for i in range(-10, 10, 1):
    print("ReLU({}): {}".format(i, ReLU(i)))

              
