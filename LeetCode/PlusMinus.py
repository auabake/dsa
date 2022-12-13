"""
Plus Minus 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Example

arr=[1,1,0-1,-1]

There are n = 5 elements, two positive, two negative and one zero.
Their ratios are:

2/5 = 0.400000 
2/5 = 0.400000 
1/5 = 0.200000

Results are printed as:

0.400000
0.400000
0.200000
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    k = len(arr)
    p = 0 # +ve numbers
    n = 0 # -ve numbers
    z = 0 # zeros
    
    for i in range (k):
        if (arr[i]>0):
            p += 1
        elif (arr[i]<0):
            n +=1
        elif (arr[i]==0):
            z += 1

    print("%1.6f" %(p/k))
    print("%1.6f" %(n/k))
    print("%1.6f" %(z/k))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
