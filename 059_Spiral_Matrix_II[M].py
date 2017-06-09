class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [ [0] * n for i in xrange(n) ]
        direct = 0
        i = j = 0
        tmp = 1
        while tmp <= n * n:
            res[i][j] = tmp
            tmp += 1
            if direct == 0:
                j += 1
                if j == n or res[i][j] != 0:
                    j -= 1
                    i += 1
                    direct = 1
                    continue
            if direct == 1:
                i += 1 
                if i == n or res[i][j] != 0:
                    i -= 1
                    j -= 1
                    direct = 2
                    continue
            if direct == 2:
                j -= 1 
                if j == -1 or res[i][j] != 0:
                    j += 1
                    i -= 1
                    direct = 3
                    continue
            if direct == 3:
                i -= 1 
                if i == -1 or res[i][j] != 0:
                    i += 1
                    j += 1
                    direct = 0
                    continue
        return res

