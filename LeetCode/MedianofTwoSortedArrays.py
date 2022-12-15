"""
Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1: return self.kth(A, B, l // 2)
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a: return b[k]
        if not b: return a[k]

        ia, ib = len(a) // 2, len(b) // 2

        if ia + ib < k:
            if a[ia] > b[ib]: return self.kth(a, b[ib + 1:], k - ib - 1)
            return self.kth(a[ia + 1:], b, k - ia - 1)

        if a[ia] > b[ib]: return self.kth(a[:ia], b, k)
        return self.kth(a, b[:ib], k)