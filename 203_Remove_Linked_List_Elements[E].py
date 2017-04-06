# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newhead.next = head
        prev = newhead
        now = newhead.next
        while now:
            if now.val == val:
                prev.next = now.next
                now = now.next
            else:
                prev = prev.next
                now = now.next
        return newhead.next