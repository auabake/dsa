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
