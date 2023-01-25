"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that 
either directly below or diagonally left/right. 

Specifically, the next element from position (row, col) will be (row + 1, col - 1), 
(row + 1, col), or (row + 1, col + 1).

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13

"""
# import sys
# n = 3
# def minpath(A) :
# 	for R in range(n - 2, -1, -1) :
# 		for C in range(n) :
# 			best = A[R + 1][C]
# 			if C > 0 :
# 				best = min(best, A[R + 1][C - 1])
# 			if C + 1 < n :
# 				best = min(best, A[R + 1][C + 1])
# 			A[R][C] = A[R][C] + best
# 	ans = sys.maxsize
# 	for i in range(n) :
# 		ans = min(ans, A[0][i])
# 	return ans
			
# if __name__ == "__main__" :
# 	A = [ [ 1, 2, 3],
# 		[ 4, 5, 6],
# 		[ 7, 8, 9] ]
# 	print(minpath(A))

import sys
class Solution(object):
	def minFallingPathSum(matrix):
		n = 3
		for R in range(n - 2, -1, -1):
			for C in range(n):
				best = matrix[R + 1][C]
				if C > 0 :
					best = min(best, matrix[R + 1][C - 1])
				if C + 1 < n :
					best = min(best, matrix[R + 1][C + 1])
				matrix[R][C] = matrix[R][C] + best
		ans = sys.maxsize
		for i in range(n) :
			ans = min(ans, matrix[0][i])
		return ans

	if __name__ == "__main__" :
		matrix = [ [ 1, 2, 3],
				 [ 4, 5, 6],
				 [ 7, 8, 9] ]
		print(minFallingPathSum(matrix))

# optimized from leetcode 97%
class Solution(object):
   def minFallingPathSum(matrix):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(1,n):
            for j in range(m):
                matrix[i][j] += min(matrix[i-1][max(0,j-1):min(m,j+2)])
        return min(matrix[n-1])

   if __name__ == "__main__" :
      matrix = [ [ 1, 2, 3],
         [ 4, 5, 6],
         [ 7, 8, 9] ]
      print(minFallingPathSum(matrix))
