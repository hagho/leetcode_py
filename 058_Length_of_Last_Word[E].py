class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = s.split()
        if not res:
            return 0
        return len(res[-1])