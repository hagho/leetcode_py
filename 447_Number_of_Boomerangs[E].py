class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x in points:
            d = {}
            for y in points:
                a = x[0] - y[0]
                b = x[1] - y[1]
                d[a**2 + b**2] = 1 + d.get(a**2 + b**2, 0)
            for k in d:
                res += d[k] * ( d[k] - 1 )
        return res