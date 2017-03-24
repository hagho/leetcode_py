class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i in s:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        res = 0
        flag = False
        for i in d:
            if d[i] % 2 == 0:
                res += d[i]
            else:
                flag = True
                if d[i] > 1:
                    res += d[i] - 1
        return res + 1 if flag else res

