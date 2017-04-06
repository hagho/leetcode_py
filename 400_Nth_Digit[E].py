class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(9):
            d = 9 * 10 ** i
            if n <= d * ( i + 1):
                break
            n -= d * (i + 1)
        n -= 1
        return int(str(10**i + n / (i + 1))[n % ( i + 1 )])