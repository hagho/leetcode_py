class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b =len(s) - 1
        while a < b:
            if not ( ( s[a] >= '0' and s[a] <= '9' ) or ( s[a] >= 'A' and s[a] <= 'Z' ) or ( s[a] >= 'a' and s[a] <= 'z' ) ):
                a += 1
                continue
            if not ( ( s[b] >= '0' and s[b] <= '9' ) or ( s[b] >= 'A' and s[b] <= 'Z' ) or ( s[b] >= 'a' and s[b] <= 'z' ) ):
                b -= 1
                continue
            if s[a].lower() == s[b].lower():
                a += 1
                b -= 1
            else:
                return False

        return True