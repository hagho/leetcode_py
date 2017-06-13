class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        match = [-1] * n
        j = -1
        for i in xrange(1, n):
            while j > -1 and s[i] != s[j + 1]:
                j = match[j]
            if s[i] == s[j + 1]:
                j += 1
            match[i] = j
            #print match
        return True if match[-1] > -1 and n % ( n - match[-1] - 1) == 0 else False

        