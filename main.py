#GAUSS - SEIDEL

"""
Author: @JoseMinuche
"""


from functions import *


#Libraries.

import numpy as np


#Introduction.

print("The method used to solve the equations is Gauss - Seidel.")


#Data.

dimension = int(input("Enter matrix dimension: "))


print("Toleration and max iteration is set 0.01 and 100.")

tolera = 0.01

iteramax = 100


#Menu. Creating matrix.

#A Matrix

counter = 0

while (counter == 0):

    A = create_A_matrix(dimension)

    print("This is your A matrix: ")
    print(A)

    check = input("Everything right? Y/N: ")

    if (check.upper() == "Y"):
        counter +=1

    elif (check.upper() == "N"):
        print("Please input again matrix values.")

    else:
        print("Answer not available. Please input matrix values again.")

#B Matrix

counter = 0

while (counter == 0):

    B = create_B_matrix(dimension)

    print("This is your B matrix: ")
    print(B)

    check = input("Everything right? Y/N: ")

    if (check.upper() == "Y"):
        counter +=1

    elif (check.upper() == "N"):
        print("Please input again matrix values.")

    else:
        print("Answer not available. Please input matrix values again.")

#X0 Matrix

X0 = create_X0_matrix(dimension)


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
