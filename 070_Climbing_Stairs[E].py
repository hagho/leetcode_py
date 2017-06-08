class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        res = [0] * ( n + 1 )
        res[1] = 1
        res[2] = 2
        for i in xrange(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]