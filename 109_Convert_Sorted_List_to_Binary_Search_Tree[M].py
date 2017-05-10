# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def fun(head, tail):
            fast = head
            slow = head
            if head == tail:
                return None
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next

            root = TreeNode(slow.val)
            root.left = fun(head, slow)
            root.right = fun(slow.next, tail)
            return root

        return fun(head, None)
        