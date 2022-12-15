"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val;    high = 0;     c = 1;
        if(val > 9):
            high = 1;
            val -= 10;

        res = ListNode(val)
        start = res

        while(l1.next != None or l2.next != None or high == 1):
            tem = high; high = 0

            if(l1.next != None):  
                l1 = l1.next
                tem += l1.val

            if(l2.next != None):
                l2 = l2.next
                tem += l2.val

            if(tem > 9):
                tem -= 10
                high = 1

            res.next = ListNode(tem)
            res = res.next
        return start