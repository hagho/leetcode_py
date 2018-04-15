class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = [-1] * 256
        res = 0
        j = -1
        for i, c in enumerate(s):
            j = max(hashtable[ord(c)], j)
            hashtable[ord(c)] = i
            res = max(i - j, res)
        return res
