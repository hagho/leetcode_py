class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
    
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curmin = self.getMin()
        print curmin
        if curmin == None or curmin > x:
            curmin = x
        self.s.append((x, curmin))

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        else:
            return self.s[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        else:
            return self.s[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()