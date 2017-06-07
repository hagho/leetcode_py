# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda interval: interval.start)
        now = res = 0
        for i in xrange(1, len(intervals)):
            if intervals[i].start < intervals[now].end:
                if intervals[i].end < intervals[now].end:
                    now = i
                res += 1
            else:
                now = i
        return res