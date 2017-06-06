class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = ['0', '1']
        if n == 0: return [0]
        if n == 1: return [0, 1]
        for i in xrange(1, n):
            res = ['0' + i for i in res] + ['1' + i for i in res[:: -1]]
        return [int(i, 2) for i in res] 