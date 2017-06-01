class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def fun(nums, permutation):
            if not nums:
                self.res.append(permutation)
                return
            for i in xrange(len(nums)):
                fun(nums[:i]+ nums[i + 1:], permutation + [nums[i]])
        fun(nums, [])
        return self.res