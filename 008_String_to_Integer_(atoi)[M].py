class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str: return 0
        tmp = str.split()[0]
        flag = 1
        if tmp[0] == '+' or tmp[0] == '-': 
            flag = 1 if tmp[0] == '+' else -1
            tmp = tmp[1:]
        res = 0
        for i in tmp:
            if i >= '0' and i <= '9':
                res = res * 10 + int(i)
            else:
                break
        res *= flag 
        if res > 0x7fffffff:
            return 0x7fffffff
        if res < -0x7fffffff - 1:
            return -0x7fffffff - 1
        return res


