# Happy Numbers
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits,and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.(http://en.wikipedia.org/wiki/Happy_number).

Examples

Happy   7: 7 -> 49 -> 97 -> 130 -> 10 -> 1
Unhappy 19: 19 -> 82 -> 68 -> 100 -> 1
64: 64 -> 52 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
2: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

Write a function to determine if an integer is a happy number.
