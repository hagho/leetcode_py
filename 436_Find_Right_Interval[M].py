# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        res = []
        l = sorted([(e.start, i) for i, e in enumerate(intervals)])
        for i in intervals:
            tmp = bisect.bisect_left(l, (i.end, ))
            res.append(l[tmp][1] if tmp < len(l) else -1)
        return res


        