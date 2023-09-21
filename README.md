# 4 Russians algorithm
Implementation of the 4 russians algorithm for boolean matrix multiplication.

Boolean matrices are matrices containing only 1s and 0s as entries. Matrix multiplication on boolean matrices A x B can be defined using boolean multiplication (logical AND) and boolean addition (logical OR). Like the following example: 

![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/boolean_multiplication.png?raw=true)


The Four-Russians algorithm computes the product of two n x n boolean matrices in time O(n^3/log n) by a certain strategy of pre-computing union of rows and later use a table look-up to them. Specifically, we first divide the matrices into [log n] blocks, the first matrix "A" by columns and the second "B" by rows. In case 'n mod logn > 0' we can just fill in spaces with zeros. Then we can take the product A X B by computing all Ai x Bi products and add them together.

The pseudo-code for the algorithm is given below:
![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/4-russians-algo.png?raw=true)

Graphs provide an example of how boolean matrix multiplication can be used in practice. Consider a directed graph G = (V, E), we can form the graph G* = (V, E*) which contains the same nodes as graph G but one additional edge for any pair of nodes in G that are connected (not just the direct neighbors). Graph G* is called the transitive closure of G.
Consider the following example:
![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/graph_4_russians.png?raw=true)

To calculate the transitive closure of a graph we can use boolean matrix multiplication. If A
 is the adjacency matrix of graph G
, then A2=AA
 is the adjacency matrix of the graph that we get from G
 if we add to G
 an edge for every pair of nodes that are connected with a path of length two. Similarly, A3=A2A
 is the adjacency matrix of the graph that we get grom G
 if we add to G
 an edge for every pair of nodes that are connected with a path of length two or three. In general, An=An−1A
 is the adjacency matrix of the graph we get if we add to G
 an edge for every pair of nodes that are connected with a path of length 2, 3, …
, n−1
. For this to work, we assume that each node in G
 is connected to itself, so in the adjancency matrix of G
 we put ones down the left to right diagonal. More formally, we use as adjacency matrix the matrix A∨I
, where A
 is the initial adjacency matrix and I
 is the identity matrix.
