class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.fun(s, 0)[0]
    def fun(self, s, i):
        res = ""
        while i < len(s) and s[i] != ']':
            if s[i].isalpha():
                res += s[i]
                i += 1
            else:
                tmp = s.find('[', i)
                n = int(s[i:tmp])
                i = tmp + 1
                t, i = self.fun(s, i)
                i += 1
                res += n * t
        return res, i



