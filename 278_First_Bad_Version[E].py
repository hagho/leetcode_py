# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        end = n 
        mid = first + (end - first) / 2
        while first < end:
            if isBadVersion(mid):
                end = mid
            else:
                first = mid + 1
            mid = first + (end - first) / 2
        return end