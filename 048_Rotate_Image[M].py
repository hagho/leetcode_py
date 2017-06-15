class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        if n == 0: return
        matrix.reverse()
        for i in xrange(m):
            for j in xrange(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return