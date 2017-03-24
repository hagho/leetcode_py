# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        else:
            self.dfs(head, head.next)
            head.next = None
            return self.res


    def dfs(self, head, next):
        if not next:
            self.res = head
            return
        if next.next:
            temp = self.dfs(next, next.next) 
            temp.next = head
            return head
        else:
            self.res = next
            next.next = head
            return head
        