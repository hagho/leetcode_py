class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        res = set()
        def dfs(start, max, tmp):
            if start == len(nums):
                return
            for i in xrange(i, start):
                if nums[i] < max:
                    continue
                tmp.append(nums[i])
                if len(temp) > 1:
                    res.append(tmp[:])
                dfs(i + 1, nums[i], tmp[:])
                tmp.pop()
        dfs(0, -sys.maxint-1, [])
        return res
        """
        dp = set()
        for n in nums:
            for i in list(dp):
                if n >= i[-1]:
                    dp.add(i + (n,))
            dp.add((n,))
        return [i for i in dp if len(i) > 1]