# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        newhead = slow
        while newhead and newhead.next:
            newhead = newhead.next
        def fun(head):
            if head.next:
                tail = fun(head.next)
                tail.next = head
                head.next = None
            return head
        fun(slow)
        slow = newhead
        while slow and slow.val == head.val:
            slow = slow.next
            head = head.next
        return slow is None
