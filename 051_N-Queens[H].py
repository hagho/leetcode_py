class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens, xy_sum, xy_diff):
            p = len(queens)
            if p == n:
                res.append(queens)
                return 
            for q in xrange(n):
                if q not in queens and p + q not in xy_sum and p - q not in xy_diff:
                    DFS(queens + [q], xy_sum + [p + q], xy_diff + [p - q])
        res = []
        DFS([], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in r] for r in res]