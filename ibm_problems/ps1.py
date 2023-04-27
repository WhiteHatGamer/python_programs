"""
1. Array Subsets
Given an integer array, divide the array into 2 subsets A and B while respecting the following conditions :

 The intersection of A and B is null.
The union A and B is equal to the original array.
The number of elements in subset A is minimal.
The sum of A's elements is greater than the sum of B's elements.
 

Return the subset A in increasing order where the sum of A's elements is greater than 
the sum of B's elements. If more than one subset exists, return the one with the maximal sum.

Example

n = 5

arr = [3, 7, 5, 6, 2]

 

The 2 subsets in arr that satisfy the conditions for A are [5, 7] and  [6, 7] :

A is minimal (size 2)
Sum(A) = (5 + 7) = 12 > Sum(B) = (2 + 3 + 6) = 11
Sum(A) = (6 + 7) = 13 > Sum(B) = (2 + 3 + 5) = 10
The intersection of A and B is null and their union is equal to arr.
The subset A where the sum of its elements is maximal is [6, 7].
 

Function Description

Complete the subsetA function in the editor below.

 

subsetA has the following parameter(s):

    int arr[]: an integer array

Returns:

    int[] : an integer array with the values of subset A.

 

Constraints

1 ≤ n ≤ 105 
1 ≤ arr[i] ≤ 105 (where 0 ≤ i < n)
 

Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

STDIN     Function 
-----     --------
6     →   arr[] size n = 6
5     →   arr[] = [5, 3, 2, 4, 1, 2]
3
2
4
1
2
Sample Output

4
5
Explanation

n = 6

arr = [5, 3, 2, 4, 1, 2]

 

The subset of A that satisfies the conditions is [4, 5] :

A is minimal (size 2)
Sum(A) = (4 + 5)= 9 > Sum(B) = (1 + 2 + 2 +  3) = 8
The intersection of A and B is null and their union is equal to arr.
The subset A with the maximal sum is [4, 5].
 

Sample Case 1
"""
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def subsetA(arr):
    # Write your code here
    n = len(arr) #O(1)
    arrB = sorted(arr) #O(n)
    an = int(n//2)+1 #1
    arrA = [] #1
    sumA = 0 #1
    sumB = sum(arrB) #removed from for loop
    for i in range(n-1,an-3,-1): #n
        arrA.append(arrB[i]) #1
        sumA += arrB[i] #1
        sumB = sumB - arrB[i] #
        if(sumA>sumB): #1
            break
    return sorted(arrA) #n
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
