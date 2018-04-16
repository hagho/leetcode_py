class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str = [""] * numRows
        if (numRows == 1):
            return s
        j = 0
        flag = 1
        for i in xrange(len(s)):
            if j == 0:
                flag = 1
            if j == numRows - 1:
                flag = -1
            str[j] += s[i]
            j += flag
        res = ""
        for i in xrange(numRows):
            res += str[i]
        return res
        