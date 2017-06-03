class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ""
        tmp = 0
        S = ''.join(S[::-1].split('-'))
        for i in S:
            if tmp == K:
                res = '-' + res
                tmp = 0
            if i == '-':
                continue
            res = i.upper() + res
            tmp += 1
        return res
