class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            res[i] = max(res[i - 1], nums[i] + res[i - 2])
        return res[len(nums) - 1]

        