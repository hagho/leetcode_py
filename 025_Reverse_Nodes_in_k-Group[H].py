# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        for i in xrange(k):
            if not node:
                return head
            node = node.next

        new_head = self.reverse(head, node)
        head.next = self.reverseKGroup(node, k)
        return new_head
    def reverse(self, first, last):
        prev = last
        while first != last:
            tmp = first.next
            first.next = prev
            prev = first
            first = tmp
        return prev