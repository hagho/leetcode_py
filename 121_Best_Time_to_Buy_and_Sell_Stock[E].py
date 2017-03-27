class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = 1
        while i < len(prices):
            if (j >= len(prices)):
                break
            if (prices[j] > prices[i]):
                res = max(prices[j] - prices[i], res)
                j += 1
            elif (prices[j] < prices[i]):
                i = j
                continue
            else:
                j += 1
        return res


