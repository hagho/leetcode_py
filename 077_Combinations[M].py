class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(start, depth, r):
            if depth == k:
                res.append(r[:])
                return
            for i in xrange(start, n + 1):
                r.append(i)
                dfs(i + 1, depth + 1, r)
                r.pop()

        dfs(1, 0, [])
        return res
