class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        s = s.zfill(32)
        s = s[::-1]
        return int(s, 2)