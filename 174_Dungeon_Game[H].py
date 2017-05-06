class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        w = len(dungeon[0])
        h = len(dungeon)

        hp = [[0] * w for x in xrange(h)]

        hp[h - 1][w - 1] = max(0, -dungeon[h - 1][w - 1]) + 1

        for x in xrange(h - 1, -1, -1):
            for y in xrange(w - 1, -1, -1):
                down = None
                if x + 1 < h:
                    down = max(1, hp[x + 1][y] - dungeon[x][y])
                right = None
                if y + 1 < w:
                    right = max(1, hp[x][y + 1] - dungeon[x][y])
                if down and right:
                    hp[x][y] = min(down, right)
                elif down:
                    hp[x][y] = down
                elif right:
                    hp[x][y] = right
        return hp[0][0]
