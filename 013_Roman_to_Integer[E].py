class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        table = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        for i in xrange(len(s)):
            res += table[s[i]]
            if i > 0 and table[s[i]] > table[s[i - 1]]:
                res -= 2 * table[s[i - 1]]
        return res
