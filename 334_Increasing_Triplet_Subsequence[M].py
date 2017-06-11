class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        res = [nums[0]]
        for i in nums[1:]:
            if len(res) > 2:
                return True
            if i  > res[-1]:
                res.append(i)
            else:
                res[bisect.bisect_left(res, i)] = i
        return True if len(res) > 2 else False 
