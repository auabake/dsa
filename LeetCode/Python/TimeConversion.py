"""
Time Conversion

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example 

s = '12:01:00PM'
Return '12:01:00'

s = '12:01:00 AM'
Return '00:01:00'
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # trik is to use python slice method
    #s[-2:] gets the last 2 items and s[:2] all but the first two items 
   
   
    if s[-2:] == "AM" and s[:2] == "12": 
            return "00" + s[2:-2]  

    elif s[-2:] == "AM": 
        return s[:-2]

    elif s[-2:] == "PM" and s[:2] == "12": 
        return s[:-2] 

    else:
        ans = int(s[:2]) + 12
        return str(str(ans) + s[2:8]) 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
