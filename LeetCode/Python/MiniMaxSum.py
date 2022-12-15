"""
Mini_Max_Sum 

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example 

arr=[1,3,5,7,9]

The minimum sum is 1+3+5+7=16 
The maximum sum is 3+5+7+9=24

The function prints 16 24 
"""

def miniMaxSum(arr):
    arr.sort()
    k = sum(arr) # get the sum of the sorted arry 
    mn = k-arr[len(arr)-1] # minimum_sum = sum - the int @ last index 
    mx = k-arr[0] # maximum_sum = sum - the int @ the first index
    print(mn,mx)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)