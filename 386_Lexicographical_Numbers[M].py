class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        res = []
        for i in xrange(1, n + 1):
            res.append(str(i))
        return sorted(res)
        """
        res = [1]
        while len(res) < n:
            new = res[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:
                    new /= 10 
            res.append(new)
        return res


