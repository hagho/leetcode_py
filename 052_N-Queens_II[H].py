class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(queens, xy_sum, xy_diff):
            p = len(queens)
            if p == n:
                self.res += 1
                return 
            for q in xrange(n):
                if q not in queens and p + q not in xy_sum and p - q not in xy_diff:
                    DFS(queens + [q], xy_sum + [p + q], xy_diff + [p - q])
        self.res = 0
        DFS([], [], [])
        return self.res