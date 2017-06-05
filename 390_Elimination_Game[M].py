class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        p = 1
        res = 1
        while n > 1:
            cnt +=1
            p *= 2
            n /= 2
            if cnt % 2:
                res += p / 2 + p * (n - 1)
            else:
                res -= p / 2 + p * (n - 1)
        return res
