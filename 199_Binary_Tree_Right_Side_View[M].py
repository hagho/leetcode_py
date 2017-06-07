# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def fun(root, depth):
            if not root: return None
            if depth > len(res):
                res.append(root.val)
            fun(root.right, depth + 1)
            fun(root.left, depth + 1)
        fun(root, 1)
        return res
