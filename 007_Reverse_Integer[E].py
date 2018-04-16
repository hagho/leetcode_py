class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        flag = 1 if x > 0 else -1
        x = abs(x)
        while (x):
            res = res * 10 + x % 10 
            if res > 0x7fffffff or res < -0x7fffffff - 1:
                return 0
            x /= 10
        return res * flag
        