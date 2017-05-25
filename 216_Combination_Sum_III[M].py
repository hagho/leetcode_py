class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(k, n, index, tmp):
            if k  == 0 and sum(tmp) == n:
                self.res.append(tmp)
                return
            if sum(tmp) > n:
                return
            for i in xrange(index, 10):
                tmp.append(i)
                dfs(k - 1, n, i + 1, tmp[:])
                tmp.pop()

        self.res = []
        dfs(k, n, 1, [])
        return self.res