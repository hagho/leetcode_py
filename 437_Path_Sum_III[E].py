# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.sumUp(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def sumUp(self, root, pre, sum):
        if not root:
            return 0
        current = root.val + pre
        return (current == sum) + self.sumUp(root.left, current, sum) + self.sumUp(root.right, current, sum)