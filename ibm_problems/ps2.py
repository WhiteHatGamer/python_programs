"""
2. Binary Number in a Linked List
A binary number is represented as a series of 0's and 1's. In this challenge, the series will be in the form of a singly-linked list. Each node instance, a LinkedListNode, has a value, data, and a pointer to the next node, next. Given a reference to the head of a singly-linked list, convert the binary number represented to a decimal number.

Example

PS Example
Linked list corresponding to the binary number (010011)[2] or (19)[10].
 
Function Description
Complete the function getNumber in the editor below.

getNumber has the following parameter(s):

    binary:  reference to the head of a singly-linked list of binary digits

 

Returns:

    int: a (long integer)[10] representation of the binary number

 

Constraints

1 ≤ n ≤ 64
All LinkedListNode.data ∈ {01}
The described (integer)[2] < 264
 

Input Format for Custom Testing
Sample Case 0
Sample Input

STDIN    Function
-----    -----
7     →  binary[] size n = 7
0     →  binary LinkedListNode.data = [0, 0, 1, 1, 0, 1, 0]
0                                      
1                                      
1                                      
0                                      
1                                      
0                                       
Sample Output

26
Explanation

Sample 0
The linked list is given as input.
The linked list forms the binary number 0011010 → (0011010)[2] = (26)[10]

Sample Case 1
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'getNumber' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def add_singly_linked_list(binary):
    if binary.next == None:
        return binary.data
    else:
        return([binary.data].append(add_singly_linked_list(binary.next)))

def getNumber(binary):
    # Write your code here
    data = []
    dec = 0
    #data.append(binary.data)
    data.append(add_singly_linked_list(binary))
    #while binary.next != None:
    #    binary = binary.next
    #    data.append(binary.data)
    digit = (len(data))-1
    for i in data:
        dec += i*pow(2,digit)
        digit = digit - 1
    return dec
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary_count = int(input().strip())

    binary = SinglyLinkedList()

    for _ in range(binary_count):
        binary_item = int(input().strip())
        binary.insert_node(binary_item)

    result = getNumber(binary.head)

    fptr.write(str(result) + '\n')

    fptr.close()
