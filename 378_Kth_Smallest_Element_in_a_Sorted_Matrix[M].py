class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        heap= [(matrix[0][0], 0, 0)]
        for _ in xrange(k):
                ans, i, j = heapq.heappop(heap)
                if j == 0 and i + 1 < m:
                    heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                if j + 1 < n:
                    heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return ans

    