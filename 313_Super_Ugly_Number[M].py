class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [0] * n
        res[0] = 1
        vals = [0] * len(primes)
        idxs = [0] * len(primes)
        for i in xrange(1, n):
            for j in xrange(len(primes)):
                vals[j] = res[idxs[j]] * primes[j]
            res[i] = min(vals)
            for j in xrange(len(primes)):
                if vals[j] == res[i]:
                    idxs[j] += 1
        return res[-1]