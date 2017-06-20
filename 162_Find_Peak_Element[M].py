class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return
        if n == 1:
            return 0
        else:
            if nums[0] > nums[1]: return 0
            elif nums[-1] > nums[-2]: return n - 1
            for i in xrange(1, n - 1):
                if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                    return i
        return