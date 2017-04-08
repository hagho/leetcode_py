class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def mycmp(a, b):
            if a[0] == b[0]:
                return a[1] - b[1]
            else:
                return b[0] - a[0]
        people.sort(mycmp)
        #print people
        res = []
        for i in people:
            res.insert(i[1], i)
        return res