# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.num = 1
        def preorder(root):
            if not root:
                return None
            preorder(root.left)
            if k < self.num:
                return
            if self.num == k:
                self.res = root.val
                self.num += 1
                return
            else: 
                self.num += 1
            preorder(root.right)
        preorder(root)
        return self.res