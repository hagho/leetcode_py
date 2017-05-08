class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        heap = [(sys.maxint, None, None)]
        size1, size2 = len(nums1), len(nums2)
        idx2 = 0
        while idx2 < size2:
            for idx1 in xrange(size1):
                heapq.heappush(heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
            idx2 += 1
        for i in xrange(min(k, size1 * size2)):
            sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
        return res