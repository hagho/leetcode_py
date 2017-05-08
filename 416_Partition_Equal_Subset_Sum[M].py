class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s & 1 == 1:
            return False
        s /= 2
        dp = [False] * ( s + 1 )
        dp[0] = True

        for i in nums:
            for j in xrange(s, 0, -1):
                if j >= i:
                    dp[j] = dp[j] or dp[j - i]
        return dp[s]
