import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        def neighbors(x, y):
            tmp = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if  0 <= x + i < m and 0 <= y + j < n:
                        tmp += board[x + i][y + j]
            tmp -= board[x][y]  
            return tmp
        tmp = copy.deepcopy(board)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 1:
                    if neighbors(i, j) < 2:
                        tmp[i][j] = 0
                    elif 2 <= neighbors(i, j) <= 3:
                        continue
                    else:
                        tmp[i][j] = 0 
                else:
                    if neighbors(i, j) == 3:
                        tmp[i][j] = 1
        board[:] = tmp
        return