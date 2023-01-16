"""
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        for _ in range(n):
            node2 = node2.next

        node_prev = None
        while node2:
            node_prev = node1
            node1 = node1.next
            node2 = node2.next

        if node_prev is None:
            return head.next

        node_prev.next = node1.next
        return head
        