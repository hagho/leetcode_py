class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [ [0] * ( n + 1 ) for i in xrange(m + 1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in xrange(m, zeros - 1, -1):
                for j in xrange(n, ones - 1, -1):
                    res[i][j] = max(res[i][j], res[i - zeros][j -ones] + 1)
        return res[m][n]
