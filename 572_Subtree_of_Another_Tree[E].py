# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def func(s, t):
            if t == None and s == None:
                return True
            if s == None:
                return False
            if t == None:
                return False
            if s.val != t.val:
                return False
            return func(s.left, t.left) and func(s.right, t.right)

        res = False
        if s != None and t != None:
            if s.val == t.val:
                res = func(s, t)
            if not res:
                res = self.isSubtree(s.left, t)
            if not res:
                res = self.isSubtree(s.right, t)
        return res 
