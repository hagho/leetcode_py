class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            res = chr( ord('A') + ( n - 1 ) % 26 ) + res
            n -= 1
            n  /= 26
        return res