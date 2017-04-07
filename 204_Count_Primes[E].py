class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<= 2:
            return 0
        count = 1
        primer = [False] * n
        upper = math.sqrt(n)
        for i in xrange(3, n, 2):
            if not primer[i]:
                count += 1
                if i > upper:
                    continue
                for j in xrange(i * i, n, i):
                    primer[j] = True
        return count
