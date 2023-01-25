"""
3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best = float('inf')

        for i in range(len(nums) - 2):
            v = self.twoSumClosest(nums, target, nums[i], i + 1)
            if abs(v - target) < abs(best - target):
                best = v
        return best

    def twoSumClosest(self, nums, target, other_num, start_index):
        i, j = start_index, len(nums) - 1
        best = float('inf')

        while i < j:
            v = nums[i] + nums[j] + other_num
            if abs(v - target) < abs(best - target):
                best = v

            if v < target:
                i += 1
            else:
                j -= 1

        return best
