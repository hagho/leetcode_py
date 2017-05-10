# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        self.res += self.fun(root)
        self.dfs(root.right)
        self.dfs(root.left)

    def fun(self, root):
        return abs(self.sum(root.right) - self.sum(root.left))

    def sum(self, root):
        if not root:
            return 0
        return root.val + self.sum(root.right) + self.sum(root.left)
'''

class Solution(object):
    def findTilt(self, root):
        self.ans = 0
        def _sum(node):
            if not node: return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right
        _sum(root)
        return self.ans