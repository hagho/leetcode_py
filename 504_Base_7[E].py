class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        res = ""
        n = abs(num)
        if n == 0:
            res = '0'
        while n:
            res = str(n % 7) + res
            n = n / 7
        if num >= 0:
            pass
        else:
            res = '-' + res
        return res
        """
        if num < 0:
            return '-' + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)