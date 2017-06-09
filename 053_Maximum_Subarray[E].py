class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in xrange(1, len(nums)):
            dp[i] = nums[i] + ( dp[i - 1] if dp[i - 1] > 0 else 0 )
            res = max(res, dp[i])
        return res