class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                res += i
        res = res[::-1]
        flag = 0
        s = list(s)
        for i in xrange(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                s[i] = res[flag]
                flag += 1
        return "".join(s)