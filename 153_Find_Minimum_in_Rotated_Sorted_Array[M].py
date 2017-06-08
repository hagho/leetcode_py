class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = 0
        ed = len(nums) - 1
        while st < ed:
            mid = ( st + ed ) / 2
            if nums[mid] <= nums[ed]:
                ed = mid
            else:
                st = mid + 1
        return nums[st]