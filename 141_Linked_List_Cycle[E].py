# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = head
        
        while p1 != None and p2 != None:
            if p1.next and p2.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
                if p1 == p2:
                    return True
            else:
                return False
        return False