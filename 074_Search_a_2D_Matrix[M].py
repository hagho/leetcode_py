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
        if m == 0:
            return False
        low = 0
        high = m * n - 1
        while low < high:
            mid = ( low + high ) / 2
            num = matrix[mid / m][mid % m]
            if target > num:
                low = mid + 1
            else:
                high = mid
        if matrix[low / m][low % m] == target:
            return True
        else:
            return False