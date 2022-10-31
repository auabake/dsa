class Solution(object):
   def twoSumLessThanK(self, A, K):
      ans = -1
      if len(A)==1:
         return -1
      for i in range(len(A)):
         for j in range(i+1,len(A)):
            temp = A[i]+ A[j]
            if temp<K:
               ans = max(ans,temp)
      return ans