class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        l = [1]
        if num <= 1:
            return False
        for i in xrange(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                l.append(i)
                l.append(num // i)
                
        print l
        return sum(l) == num