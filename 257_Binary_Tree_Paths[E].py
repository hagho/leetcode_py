# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def dfs(root, path):
            if not root:
                return
            path += str(root.val) + "->"
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            if not root.left and not root.right:
                res.append(path[:-2]) 
        dfs(root, "")
        return res
