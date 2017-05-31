class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        if input[i] == '+':
                            res.append(j + k)
                        if input[i] == '-':
                            res.append(j - k)
                        if input[i] == '*':
                            res.append(j * k)
        return res
                    