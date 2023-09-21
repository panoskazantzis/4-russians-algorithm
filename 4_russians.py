# 4 Russians algorithm for boolean matrix multiplication

import numpy as np
import math
from itertools import product


def four_russians(matrix_A, matrix_B):
    """
    Matrix boolean multiplication.

    Computes the boolean product of two matrices A and B using the 4 Russians algorithm.

    Parameters
    ----------
    matrix_A : np.array
        np.array representing a boolean matrix containing 1s and 0s.
    matrix_B : np.array
        np.array representing a boolean matrix containing 1s and 0s.

    Returns
    -------
    matrix_C : np.array
        np.array representing the boolean product of matrix_A and matrix_b.
    """
    n = len(matrix_A)
    lg = int(math.log2(n))

    #if necessary fill with zeros
    if n%lg != 0:
        add_count = lg - n%lg
        # add columns of zeros
        matrix_A = np.insert(
            matrix_A, matrix_A.shape[1], np.array([[0]*n]*add_count), axis=1,
        )
        # add rows of zeros
        matrix_B = np.vstack((B, np.array([[0]*n]*add_count)))
        
    # Boolean matrix multiplication using 4 Russians approach
    matrix_C = np.array([[0]*n]*n)
    for i in range(0, len(matrix_B)//lg, 1):
        # Split the matrices
        # take column i from matrix A
        Ai = np.array([list(row[i*lg: (i+1)*lg]) for row in matrix_A])
        # take row i from matrix B
        Bi = matrix_B[i*lg: (i+1)*lg]
        
        # Calculate all possible sum of rows of Bi
        all_sums = all_row_sums(Bi)
        
        # find AixBi
        AiBi = []
        for row in Ai:
            # add sums of Bi rows corresponding to Ai rows
            AiBi.append(list(all_sums[tuple(row)]))
        
        # add iterartively to matrix C = AxB
        matrix_C = matrix_C + AiBi
        
    # transform to boolean addition
    matrix_C[matrix_C >= 1] = 1
    
    return matrix_C
