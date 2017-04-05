class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        for i in xrange(len(nums)):
            first = nums[i]
            for j in xrange(i + 1, k + 1)：
                if j == len(nums):
                    break
                if nums[j] == first:
                    return True
        return False
        '''
        d = dict()
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False