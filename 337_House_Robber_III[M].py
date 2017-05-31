# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        valMap = {}
        def fun(root, path):
            if root is None:
                return 0
            if path not in valMap:
                left, right = root.left, root.right
                ll = lr = rr = rl = None
                if left:
                    ll, lr = left.left, left.right
                if right:
                    rl, rr = right.left, right.right
                valMap[path] = max(fun(left, path + 'l') + fun(right, path + 'r'), \
                                    root.val + fun(ll, path + "ll") + fun(lr, path + "lr") + fun(rl, path + "rl") + fun(rr, path + "rr"))
            return valMap[path]
        return fun(root, '')    