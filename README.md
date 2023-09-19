# 4-russians-algorithm
Implementation of the 4 russians algorithm for boolean matrix multiplication.

Boolean matrices are matrices containing only 1s and 0s as entries. Matrix multiplication on boolean matrices A x B can be defined using boolean multiplication (logical AND) and boolean addition (logical OR). Like the following example: 

![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/boolean_multiplication.png?raw=true)


The Four-Russians algoerithm computes the product of two n x n boolean matrices in time O(n^3/log n) by a certain strategy of pre-computing union of rows and later use a table look-up to them. The process is explained in more detail below:

The pseudo-code for the algorithm is given below:
![alt text](https://github.com/panoskazantzis/4-russians-algorithm/blob/main/assets/4-russians-algorithm.png?raw=true)
