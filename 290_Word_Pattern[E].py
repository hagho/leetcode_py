class Solution(object):
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)
    '''
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        d = dict()
        if len(pattern) != len(s):
            return False
        for i in xrange(len(pattern)):
            if not d.get(pattern[i]):
                if s[i] in d.values():
                    return False
                d[pattern[i]] = s[i]
            else:
                if d[pattern[i]] != s[i]:
                    return False
        return True
        '''