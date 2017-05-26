class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = [0] * 10
        alpha = [0] * 128
        for c in s:
            alpha[ord(c)] += 1
        a[0] = alpha[ord('z')]
        a[2] = alpha[ord('w')]
        a[4] = alpha[ord('u')]
        a[6] = alpha[ord('x')]
        a[8] = alpha[ord('g')]
        a[3] = alpha[ord('h')] - a[8]
        a[5] = alpha[ord('f')] - a[4]
        a[7] = alpha[ord('v')] - a[5]
        a[1] = alpha[ord('o')] - a[0] - a[2] - a[4]
        a[9] = alpha[ord('i')] - a[5] - a[6] - a[8]
        res = ""
        for i  in xrange(10):
            if a[i] > 0:
                res += str(i) * a[i]
        return res