# 4 Russians algorithm
Implementation of the 4 russians algorithm for boolean matrix multiplication.

Boolean matrices are matrices containing only 1s and 0s as entries. Matrix multiplication on boolean matrices A x B can be defined using boolean multiplication (logical AND) and boolean addition (logical OR). Like the following example: 

![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/boolean_multiplication.png?raw=true)


The Four-Russians algorithm computes the product of two n x n boolean matrices in time O(n^3/log n) by a certain strategy of pre-computing union of rows and later use a table look-up to them. Specifically, we first divide the matrices into [log n] blocks, the first matrix "A" by columns and the second "B" by rows. In case 'n mod logn > 0' we can just fill in spaces with zeros. Then we can take the product A X B by computing all Ai x Bi products and add them together.

The pseudo-code for the algorithm is given below:
![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/4-russians-algo.png?raw=true)

Graphs provide an example of how boolean matrix multiplication can be used in practice. Consider a directed graph G = (V, E), we can form the graph G* = (V, E*) which contains the same nodes as graph G but one additional edge for any pair of nodes in G that are connected (not just the direct neighbors). Graph G* is called the transitive closure of G.
Consider the following example:
