#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    k = sum(arr) # get the sum of the sorted arry 
    mn = k-arr[len(arr)-1] # minimum_sum = sum - the int @ last index 
    mx = k-arr[0] # maximum_sum = sum - the int @ the first index
    print(mn,mx)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
