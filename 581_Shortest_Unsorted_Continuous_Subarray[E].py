class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = nums[:]
        n.sort()
        a = 0
        b = len(nums) - 1
        for i in xrange(len(nums)):
            if n[i] == nums[i]:
                a+=1
            else:
                break
        for i in xrange(len(nums) - 1, -1, -1):
            if n[i] == nums[i]:
               b-=1
            else:
                break
        if b < a:
            return 0
        return b- a + 1
