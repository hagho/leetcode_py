class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        num_table = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_table = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        while num > 0:
            for i, n in enumerate(num_table):
                if num >= n:
                    break
            num -= n
            res += roman_table[i]
        return res