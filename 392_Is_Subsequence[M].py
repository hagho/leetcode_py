class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        i = 0
        for j in t:
            if s[i] == j:
                i +=1
                if i == len(s):
                    return True
        return False
