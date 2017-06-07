class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size < 2:
            return 0
        sell = [0] * size
        hold = [0] * size
        sell[0], sell[1] = 0, max(0, prices[1] - prices[0])
        hold[0], hold[1] = -prices[0], max(-prices[0], -prices[1])
        for i in xrange(2, size):
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], sell[i - 2] - prices[i])
        return sell[size -1]