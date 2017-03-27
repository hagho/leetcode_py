class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idx1 = a.find('+')
        idx2 = b.find('+')
        r1 = int(a[: idx1])
        c1 = int(a[dix1 + 1: len(a) - 1])
        r2 = int(b[: idx2])
        c2 = int(b[idx2 + 1: len(a) - 1])
        r = r1 * r2 - c1 * c2
        c = r1 * c2 + r2 * c1
        return str(r) + '+' + c + 'i'