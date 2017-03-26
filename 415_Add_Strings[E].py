class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = len(num1)
        b = len(num2)
        carry = 0
        res = ""
        while a or b or carry:
            digit = carry
            if a:
                a -= 1
                digit += int(num1[a])
            if b:
                b -= 1
                digit += int(num2[b])
            carry = digit / 10
            res += str(digit % 10)
        return res[::-1]