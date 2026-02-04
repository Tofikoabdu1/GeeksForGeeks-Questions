from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        # a =[1 ,2 ,4 ,4 ,0]
        # b =[2, 4, 5, 0, 1]
        d = Counter(a)
        e = Counter(b)
        # print(d)
        # print(e)
        # print(d==e)
        if d==e:
            return True
        else:
            return False