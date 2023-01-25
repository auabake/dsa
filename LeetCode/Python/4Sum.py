"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        i = 0
        while i < len(nums) - 3:
            for x in self.threeSum(nums, target - nums[i], i + 1):
                out.append([nums[i]] + x)

            i += 1
            while nums[i] == nums[i - 1]:
                i += 1
                if i >= len(nums) - 3:
                    break
            else:
                continue
            break

        return out

    def threeSum(self, nums, target, start_index):
        out = []
        i = start_index
        while i < len(nums) - 2:
            for x in self.twoSum(nums, target - nums[i], i + 1):
                out.append([nums[i]] + x)

            i += 1
            while nums[i] == nums[i - 1]:
                i += 1
                if i >= len(nums) - 2:
                    break
            else:
                continue
            break

        return out

    def twoSum(self, nums, target, start_index):
        out = []
        i, j = start_index, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                out.append([nums[i], nums[j]])

                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1

                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

        return out