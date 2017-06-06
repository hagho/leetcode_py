class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0] * n for i in xrange(m)]
        if m == 0 or n == 0:
            return 0
        for i in xrange(n):
            res[0][i] = 1
        for i in xrange(m):
            res[i][0] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m - 1][n - 1]