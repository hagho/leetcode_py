class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        res = 0
        for i in count:
            if i + 1 in count:
                res = max(res, count[i] + count[i + 1])
        return res