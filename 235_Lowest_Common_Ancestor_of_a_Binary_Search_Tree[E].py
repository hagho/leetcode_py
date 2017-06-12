# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        def dfs(root):
            if not root:
                return 
            if root.val <= q.val and root.val >= p.val:
                return root
            else:
                if root.val < p.val:
                    return dfs(root.right)
                else:
                    return dfs(root.left)
        return dfs(root)