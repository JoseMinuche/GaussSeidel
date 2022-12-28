#GAUSS - SEIDEL

"""
Author: @JoseMinuche
"""


#Libraries.

import numpy as np


"""
How to install -> README
"""


#Gauss - Seidel Procedure.

def gauss_seidel(A, B, X0, tolera, iteramax):

    tamano = np.shape(A)
    n = tamano[0]
    m = tamano[1]

    #initial value
    X = np.copy(X0)
    difference = np.ones(n, dtype=float)
    error = 2 * tolera

    itera = 0

    while not(error <= tolera or itera > iteramax):

            #rows

            for i in range(0,n,1):

                    #columns

                    sums = 0

                    for j in range(0,m,1):

                            # except diagonal A

                            if (i != j):

                                    sums = sums - A[i,j] * X[j]

                    new_ = (B[i] + sums) / A[i,i]
                    difference[i] = np.abs(new_ - X[i])
                    X[i] = new_

            error = np.max(difference)
            itera = itera + 1


    #Anwser X column
    X = np.transpose([X])

    #Check if it does not converge
    if (itera>iteramax):
            X=0
    #Check Answer
    verifica = np.dot(A,X)

    return(X, verifica, itera)


#Create A matrix

def create_A_matrix (dimension):

    A = np.ones((dimension, dimension), dtype = float)

    for i in range(0, dimension):
        value1 = input("Enter A matrix values for the row: ")
        A[i,0] = value1

        for j in range(1, dimension):
            value2 = input("Enter A matrix values for the columns of the row: ")
            A[i, j] = value2

    return A


#Create B matrix

def create_B_matrix(dimension):

    B = np.ones((dimension,1), dtype = float)

    for s in range(0, dimension):
        value3 = input("Enter B matrix values: ")

        B[s, 0] = value3

    return B


#Create X0 matrix

def create_X0_matrix(dimension):

    X0 = np.zeros((dimension), dtype = float)

    return X0
