class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        i = 0
        j = m - 1
        while i < n and j > -1:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False