"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = head.next.next
        new_head.next = head
        p1 = new_head.next
        p2 = p1.next
        if p2 and p2.next:
            p3 = p2.next
        else:
            return new_head

        while p2 and p3:
            self.swap_pair(p1, p2, p3)
            p1 = p1.next.next
            p2 = p1.next
            if p2 and p2.next:
                p3 = p2.next
            else:
                break

        return new_head

    def swap_pair(self, p1, p2, p3):
        p1.next = p3
        p2.next = p3.next
        p3.next = p2


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

a = Solution().swapPairs(node)
print(a)