class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = dict()
        for index, i in enumerate(nums):
            if target - i in maps:
                return [index, maps[target - i]]
            else:
                maps[i] = index
