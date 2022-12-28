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

print("\n**Results**\n")

print("Used A, B\n")
print(A, "\n\n", B, "\n\n")

print("**Answers**\n")

print('X:\n')
print(gauss_seidel(A, B, X0, tolera, iteramax)[0])

print('\nA.X=B: \n')
print(gauss_seidel(A, B, X0, tolera, iteramax)[1])

print('\nNeeded iterations: \n')
print(gauss_seidel(A, B, X0, tolera, iteramax)[2])
