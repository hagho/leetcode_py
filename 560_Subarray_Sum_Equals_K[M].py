class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        count[0] = 1
        res = 0
        s = 0
        for i in nums:
            s += i
            res += count[s - k]
            count[s]+=1
        return res