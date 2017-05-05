class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split(' ')
        for i in xrange(len(ss)):
            ss[i] = ss[i][::-1]

        return ' '.join(ss)

