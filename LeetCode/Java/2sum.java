// 1. Two Sum / Easy

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Example 1:

// Input: nums = [2,11,15,7], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        
        for (int i = 0; i < nums.length - 1; ++i) {
            for (int j = i + 1; j < nums.length; ++j) {
                if (nums[i] + nums[j] == target) {
                    ans[0] = i;
                    ans[1] = j;
                    break;
                }
            }
        }
        
        return ans;
    }
}

// Big 0(n2) 2sum

//secnd solution Big 0(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> dictstore = new HashMap<>();
        
        for (int i = 0; i < nums.length; ++i) {
            int temp = target - nums[i];
            
            if (dictstore.containsKey(temp)) {
                return new int[] {dictstore.get(temp), i};
            }
            
            dictstore.put(nums[i], i);
        }
        
        return null;
    }
}
