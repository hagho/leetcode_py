class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        l  = 0
        counts = collections.Counter()
        for h in xrange(len(s)):
            counts[s[h]] += 1
            while h - l - max(counts.values()) + 1 > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, h - l + 1)
        return res