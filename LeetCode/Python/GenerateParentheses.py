"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
 
Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        memo = {}
        return self.generateParenthesis_helper(n * 2, 0, memo)

    def generateParenthesis_helper(self, n, l, memo):
        if (n, l) in memo:
            return memo[(n, l)]

        if n == 0:
            return ['']

        out = []

        if l > 0:
            for p in self.generateParenthesis_helper(n - 1, l - 1, memo):
                out.append(')' + p)

        if n > l:
            for p in self.generateParenthesis_helper(n - 1, l + 1, memo):
                out.append('(' + p)

        memo[(n, l)] = out
        return out