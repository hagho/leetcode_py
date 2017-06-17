# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def dfs(node, father, flag):
            if not node:
                return
            if not father:
                node.next = None
            if father and flag:
                node.next = father.right
            if father and not flag:
                node.next = father.next.left if father.next else None
            dfs(node.left, node, True)
            dfs(node.right, node, False)
        dfs(root, None, False)
        return