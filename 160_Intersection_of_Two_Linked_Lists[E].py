# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB
        if not pa or not pb:
            return None
        while pa and pb and pa != pb:
            pa = pa.next
            pb = pb.next
            if pa == pb:
                return pa
            if not pa:
                pa = headB
            if not pb:
                pb = headA
        return pa