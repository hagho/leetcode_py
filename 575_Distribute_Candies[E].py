class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        res = set(candies)
        if len(res) > ( len(candies) / 2):
            return len(candies) /  2
        return len(res)