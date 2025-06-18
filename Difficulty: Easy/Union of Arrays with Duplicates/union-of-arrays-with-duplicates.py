class Solution:    
    def findUnion(self, a, b):
        # code here
        s=[]
        for i in range(len(a)):
            if a[i] not in s:
                s.append(a[i])
        for i in range(len(b)):
            if b[i] not in s:
                s.append(b[i])
        return len(s)