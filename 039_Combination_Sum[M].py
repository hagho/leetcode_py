class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, tmp, index):
            if sum(tmp) == target:
                self.res.append(tmp)
                return
            if sum(tmp) > target:
                return
            for i in xrange(index, len(candidates)):
                tmp.append(candidates[i])
                dfs(candidates, tmp[:], i)
                tmp.pop()

        self.res = []
        dfs(candidates, [], 0)
        return self.res