# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.flag = 0
        self.res = []
        d = collections.defaultdict(int)
        def dfs(root):
            if not root: return
            d[root.val] += 1
            if self.flag < d[root.val]:
                self.res = []
                self.res.append(root.val)
                self.flag = d[root.val]
            elif self.flag == d[root.val]:
                self.res.append(root.val)
            else:
                pass
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res