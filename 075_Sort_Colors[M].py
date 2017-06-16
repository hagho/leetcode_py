class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        if len(nums) == 1:
            return
        while j < len(nums):
            if nums[i] == 0:
                i += 1
                j += 1
            else:
                while j < len(nums) and nums[j] != 0:
                    j += 1
                if j == len(nums): 
                    break
                nums[i], nums[j] = nums[j], nums[i]
        if nums[i] == 0: 
            i +=1
        j = i + 1
        while j < len(nums):
            if nums[i] == 1:
                i += 1
                j += 1
            else:
                while j < len(nums) and nums[j] != 1:
                    j += 1
                if j == len(nums): 
                    break
                nums[i], nums[j] = nums[j], nums[i]
        return