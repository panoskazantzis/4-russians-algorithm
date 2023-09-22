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
        matrix_B = np.vstack((matrix_B, np.array([[0]*n]*add_count)))
        
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


def all_row_sums(matrix):
    """
    Calculate all sum vectors of a matrix's rows.

    Calculates all sum vectors of all possible combinations of a matrix's rows.

    Parameters
    ----------
    matrix : np.array
        np.array representing any matrix.

    Returns
    -------
    all_sums : dict
        dictionary containing all sum vectors of all possible combinations of given matrix.
    """
    combinations = list(product([0, 1], repeat=len(matrix)))
    # calculate all possible row sums of matrix
    all_sums = {
        combo: boolean_sum(matrix[[i for i, value in enumerate(combo) if value == 1]]) 
        for combo in combinations
    }

    return all_sums


def boolean_sum(vectors):
    """
    Calculate boolean sum.

    Calculate the sum of all given vectors

    Parameters
    ----------
    vectors : list of lists
        List of lists containing the vectors to perform boolean addition on.

    Returns
    -------
    bool_sum : list
        List representing the sum vector of all given vectors.
    """
    # sum across columns
    bool_sum = np.sum(vectors, axis=0)
    # transform to boolean addition
    bool_sum[bool_sum >= 1] = 1

    return bool_sum


def transitive_closure_graph(graph):
    """
    Computes the transitive closure matrix of a given graph.

    Takes as input any graph as a np.array containing the edges
    e.g., 
        np.array([[0, 1], [0, 2], [1, 3], ... ])

    and computes the transitive closure graph in the same format
    using matrix multiplication with the 4 Russians method.
    
    Parameters
    ----------
    graph : np.array
        np.array representing the edges of a graph.
    
    Returns
    -------
    trans_graph : np.array
        np.array representing the edges of the transitive closure graph of the given graph.
    trans_clos : np.array
        np.array representing the adjacency matrix of the transitive closure graph of the given graph.
    """
    # Flatten the array representing the graph
    flat_arr = graph.flatten()

    # Find the unique elements ~ nodes
    nodes = np.unique(flat_arr)
    
    # compute the adjacency matrix
    adj_mtrx = get_adjacency_matrix(graph, nodes)
    
    # Get the dimensions of the array
    n, m = adj_mtrx.shape
    
    # we asssume each node in the graph is connected to itself
    # Change the diagonal elements to 1
    for i in range(min(n, m)):
        adj_mtrx[i, i] = 1
        
    # A^n = A^(n-1) x A is the transitive closure graph of A
    # initialize the transitive closure graph
    trans_clos = adj_mtrx.copy()
    for i in range(2, n):
        trans_clos = four_russians(trans_clos, adj_mtrx)
        
    # remove diagonal assumption
    for i in range(min(n, m)):
        trans_clos[i, i] = 0
        
    # from adjacency matrix to graph format
    graph = get_graph(trans_clos, nodes)
        
    return graph, trans_clos


def get_adjacency_matrix(graph, nodes):
    """
    Compute the adjacency matrix of given graph.

    Takes as input a graph in np.array format containing the edges of a graph and
    computes the adjacency matrix.

    Parameters
    ----------
    graph : np.array
        np.array representing the edges of a graph.
    nodes : list
        The labels of the nodes of the graph.

    Returns
    -------
    adj_mtrx : np.array
        np.array representing the adjacency matrix of the graph.
    """
    # initialize adjacency matrix
    adj_mtrx = np.array([[0]*len(nodes)]*len(nodes))
    
    # compute adjacency matrix
    for i_edge in range(len(graph)):
        node_start = np.where(nodes == graph[i_edge][0])[0][0]
        node_end = np.where(nodes == graph[i_edge][1])[0][0]
        adj_mtrx[node_start, node_end] = 1
        
    return adj_mtrx


def get_graph(adj_mtrx, nodes):
    """
    Compute the graph in edges format out of an adjacency matrix.

    Takes as input an adjacency matrix in np.array format and computes its 
    representation as a np.array containing the edges.

    Parameters
    ----------
    adj_mtrx : np.array
        np.array representing the adjacency matrix of a graph.
    nodes : list
        The labels of the nodes of the graph.

    Returns
    -------
    graph : np.array
        np.array representing the edges of the graph of the adjacency matrix given.
    """
    # Get the dimensions of the array
    n, m = adj_mtrx.shape
    
    graph = []
    for i in range(n):
        for j in range(n):
            if adj_mtrx[i, j] == 1:
                graph += [[nodes[i], nodes[j]]]
                
    return np.array(graph)

