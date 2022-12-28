#Example!

"""
Author: @JoseMinuche.
"""


from functions import *


#Libraries.
import numpy as np



#Data.

A = np.array([[8.0,5.0,-3.0,4.0],
              [4.0,3.0,-1.0,2.0],
              [2.0,2.0,-1.0,1.0],
              [3.0,3.0,-2.0,2.0]])

B = np.array([[12.0],
              [6.0],
              [4.0],
              [6.0]])

X0  = np.array([0.0,0.0,0.0,0.0])

tolera = 0.01
iteramax = 100

#Results.

print("Results:")

print("Used A, B, X0, tolera, iteramax:")
print(A, "\n\n", B, "\n\n", X0, "\n", tolera, "\n", iteramax, "\n\n\n")

print("*Answers*")

print('X: ')
print(gauss_seidel(A, B, X0, tolera, iteramax)[0])

print('A.X=B: ')
print(gauss_seidel(A, B, X0, tolera, iteramax)[1])

print('Needed iterations: ')
print(gauss_seidel(A, B, X0, tolera, iteramax)[2])
