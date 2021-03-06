class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0] * len(A)
        if len(A) < 3:
            return 0
        if A[2] - A[1] == A[1] - A[0]:
            dp[2] = 1
        res = dp[2]
        for i in xrange(3, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
            res += dp[i]
        return res
