"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        i = 0
        while True:
            char = None
            matched = True
            for str in strs:
                if i >= len(str):
                    matched = False
                    break
                if char is None:
                    char = str[i]
                    continue

                if str[i] != char:
                    matched = False
                    break

            if char is None or not matched:
                return ''.join(prefix)
            prefix.append(char)
            i += 1