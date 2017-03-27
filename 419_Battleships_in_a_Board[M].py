class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not len(board):
            return 0
        res = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'X' and ( i == 0 or board[i - 1][j] == '.') and ( j == 0 or board[i][j - 1] == '.'):
                    res+=1
        return res