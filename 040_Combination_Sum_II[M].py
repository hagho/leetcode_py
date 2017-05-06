class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.search(candidates, 0, target)

    def search(self, candidates, start, target):
        if target == 0:
            return [[]]
        res = []
        for i in xrange(start, len(candidates)):
            if i != start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            for r in self.search(candidates, i + 1, target - candidates[i]):
                res.append([candidates[i]] + r)
        return res