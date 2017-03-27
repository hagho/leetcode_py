class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n > 6):
            next = 0
            while (n):
                next += (n % 10)**2
                n //=10
            n = next
        return n == 1