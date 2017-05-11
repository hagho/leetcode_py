class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dz = zip((1, 0, 0, -1), (0, 1, -1, 0))
        dp = [[0] * n for x in xrange(m)]
        dp[i][j] = 1
        res = 0
        for t in xrange(N):
            ndp = [[0] * n for x in xrange(m)]
            for x in xrange(m):
                for y in xrange(n):
                    for dx, dy in dz:
                        nx , ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            ndp[nx][ny] = ( ndp[nx][ny] + dp[x][y] ) % MOD
                        else:
                            res = ( res + dp[x][y] ) % MOD
            dp = ndp
        return res