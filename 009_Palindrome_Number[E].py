class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        res = 0
        if x < 0: return False
        xx = x
        while (xx):
            res = res * 10 + xx % 10
            xx /= 10
        return res == x

        