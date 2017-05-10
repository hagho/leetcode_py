class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = 0x7fffffff
        tmp = start = 0
        for i in xrange(len(nums)):
            tmp += nums[i]
            while tmp >= s:
                res = min(res, i -start + 1)
                tmp -= nums[start]
                start += 1
        if res == 0x7fffffff:
            return 0
        return res