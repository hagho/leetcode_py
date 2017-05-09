class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.split(" ")
        r = len(res)
        for i in res:
            if not i:
                r -= 1
        return r